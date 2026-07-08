"""
PawPal+ backend core implementation.

Defines the core domain classes for the PawPal+ smart pet care management
system: Task, Pet, Owner, and Scheduler. Scheduler is the "brain" of the
system — it prioritizes tasks, detects time conflicts, builds a daily plan
that fits within an owner's available time, and explains its reasoning.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional

# Reference date used only to give due_time strings ("HH:MM") a full
# datetime so time-window arithmetic (subtraction, comparison) works.
_REFERENCE_DATE = datetime(2000, 1, 1)


@dataclass
class Task:
    """Represents a single pet care activity (feeding, walk, medication, etc.)."""

    title: str
    duration: int
    priority: int
    due_time: str
    recurring: bool
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def update_priority(self, new_priority: int) -> None:
        """Update the priority level of this task."""
        self.priority = new_priority

    def conflicts_with(self, other_task: "Task") -> bool:
        """Return True if this task's time window overlaps another task's."""
        self_start, self_end = self._time_window()
        other_start, other_end = other_task._time_window()
        return self_start < other_end and other_start < self_end

    def _time_window(self) -> tuple[datetime, datetime]:
        """Return the (start, end) datetime window this task occupies."""
        end = datetime.combine(_REFERENCE_DATE.date(), self._parse_due_time())
        start = end - timedelta(minutes=self.duration)
        return start, end

    def _parse_due_time(self):
        """Parse the due_time string ("HH:MM") into a time object."""
        return datetime.strptime(self.due_time, "%H:%M").time()


@dataclass
class Pet:
    """Represents a pet owned by an Owner, with a list of care tasks."""

    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a new care task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a care task from this pet's task list, if present."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list[Task]:
        """Return all care tasks associated with this pet."""
        return self.tasks


class Owner:
    """Represents a pet owner who manages pets and generates schedules."""

    def __init__(
        self,
        name: str,
        available_time: int,
        preferences: Optional[dict] = None,
        pets: Optional[list[Pet]] = None,
    ) -> None:
        """Initialize an Owner with name, available time, preferences, and pets."""
        self.name: str = name
        self.available_time: int = available_time
        self.preferences: dict = preferences if preferences is not None else {}
        self.pets: list[Pet] = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        """Add a new pet to this owner's list of pets."""
        self.pets.append(pet)

    def update_preferences(self, preferences: dict) -> None:
        """Merge new preference values into the owner's existing preferences."""
        self.preferences.update(preferences)

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all of this owner's pets."""
        return [task for pet in self.pets for task in pet.get_tasks()]

    def generate_schedule(self) -> "Scheduler":
        """Build a Scheduler over all pets' tasks and generate a daily plan."""
        scheduler = Scheduler(tasks=self.get_all_tasks(), available_time=self.available_time)
        scheduler.generate_daily_plan()
        return scheduler


class Scheduler:
    """The "brain" of PawPal+: prioritizes, organizes, and explains tasks across all of an owner's pets, fitting them into available time."""

    def __init__(self, tasks: Optional[list[Task]] = None, available_time: int = 0) -> None:
        """Initialize a Scheduler with a list of tasks and available time."""
        self.tasks: list[Task] = tasks if tasks is not None else []
        self.available_time: int = available_time
        self._plan: list[Task] = []
        self._skipped: list[tuple[Task, str]] = []

    def prioritize_tasks(self) -> list[Task]:
        """Sort tasks by priority (highest first), breaking ties by due_time."""
        self.tasks.sort(key=lambda task: (-task.priority, task.due_time))
        return self.tasks

    def detect_conflicts(self) -> list[tuple[Task, Task]]:
        """Return all pairs of tasks whose time windows overlap."""
        conflicts: list[tuple[Task, Task]] = []
        for i, task_a in enumerate(self.tasks):
            for task_b in self.tasks[i + 1:]:
                if task_a.conflicts_with(task_b):
                    conflicts.append((task_a, task_b))
        return conflicts

    def generate_daily_plan(self) -> list[Task]:
        """Greedily build a daily plan that fits within available_time, skipping completed, over-budget, or conflicting tasks."""
        self.prioritize_tasks()

        self._plan = []
        self._skipped = []
        remaining_time = self.available_time

        for task in self.tasks:
            if task.completed:
                self._skipped.append((task, "already completed"))
                continue

            if task.duration > remaining_time:
                self._skipped.append((task, "not enough remaining time"))
                continue

            conflicting = next(
                (scheduled for scheduled in self._plan if task.conflicts_with(scheduled)),
                None,
            )
            if conflicting is not None:
                self._skipped.append((task, f'conflicts with "{conflicting.title}"'))
                continue

            self._plan.append(task)
            remaining_time -= task.duration

        return self._plan

    def explain_schedule(self) -> str:
        """Return a human-readable explanation of the generated daily plan, generating it first if needed."""
        if not self._plan and not self._skipped:
            self.generate_daily_plan()

        lines: list[str] = ["Daily Schedule Explanation:"]

        if self._plan:
            lines.append("\nScheduled tasks (in order):")
            for position, task in enumerate(self._plan, start=1):
                lines.append(
                    f"  {position}. {task.title} — priority {task.priority}, "
                    f"due {task.due_time}, {task.duration} min"
                )
        else:
            lines.append("\nNo tasks were scheduled.")

        if self._skipped:
            lines.append("\nSkipped tasks:")
            for task, reason in self._skipped:
                lines.append(f"  - {task.title}: {reason}")

        return "\n".join(lines)
