"""
PawPal+ backend skeleton.

Defines the core domain classes for the PawPal+ smart pet care management
system: Owner, Pet, Task, and Scheduler. This module contains only class
and method stubs — no scheduling logic is implemented yet.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    """Represents a single pet care task (e.g. feeding, walk, medication)."""

    title: str
    duration: int
    priority: int
    due_time: str
    recurring: bool
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        # TODO: implement completion logic
        pass

    def update_priority(self, new_priority: int) -> None:
        """Update the priority level of this task."""
        # TODO: implement priority update logic
        pass

    def conflicts_with(self, other_task: "Task") -> bool:
        """Determine whether this task conflicts with another task."""
        # TODO: implement conflict detection logic
        pass


@dataclass
class Pet:
    """Represents a pet owned by an Owner, with a list of care tasks."""

    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a new care task to this pet's task list."""
        # TODO: implement task addition logic
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a care task from this pet's task list."""
        # TODO: implement task removal logic
        pass

    def get_tasks(self) -> list[Task]:
        """Return all care tasks associated with this pet."""
        # TODO: implement task retrieval logic
        pass


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
        # TODO: implement pet addition logic
        pass

    def update_preferences(self, preferences: dict) -> None:
        """Update the owner's scheduling preferences."""
        # TODO: implement preferences update logic
        pass

    def generate_schedule(self) -> None:
        """Generate a daily schedule for the owner's pets' tasks."""
        # TODO: implement schedule generation logic (likely delegates to Scheduler)
        pass


class Scheduler:
    """Builds and explains a daily task schedule based on priority and time."""

    def __init__(self, tasks: Optional[list[Task]] = None, available_time: int = 0) -> None:
        """Initialize a Scheduler with a list of tasks and available time."""
        self.tasks: list[Task] = tasks if tasks is not None else []
        self.available_time: int = available_time

    def prioritize_tasks(self) -> None:
        """Order tasks according to priority, due time, and other factors."""
        # TODO: implement prioritization logic
        pass

    def detect_conflicts(self) -> None:
        """Identify tasks that conflict with one another."""
        # TODO: implement conflict detection logic
        pass

    def generate_daily_plan(self) -> None:
        """Generate a daily plan of tasks that fits within available time."""
        # TODO: implement daily plan generation logic
        pass

    def explain_schedule(self) -> None:
        """Explain why tasks were scheduled in a particular order."""
        # TODO: implement schedule explanation logic
        pass
