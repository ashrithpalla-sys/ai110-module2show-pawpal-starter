"""Pytest tests for the core PawPal+ classes in pawpal_system.py."""

from datetime import date, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_mark_complete():
    task = Task(title="Feed Buddy", duration=10, priority=3, due_time="08:00", recurring=True)

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet(name="Buddy", species="Dog", age=4)

    assert pet.get_tasks() == []

    task = Task(title="Morning Walk", duration=30, priority=5, due_time="09:00", recurring=True)
    pet.add_task(task)

    assert len(pet.get_tasks()) == 1
    assert pet.get_tasks()[0] is task


# --- Sorting correctness -----------------------------------------------


def test_sort_by_time_orders_tasks_chronologically():
    # Tasks are added out of chronological order on purpose.
    evening_task = Task(title="Playtime", duration=20, priority=2, due_time="17:00", recurring=False)
    morning_task = Task(title="Feed Buddy", duration=10, priority=3, due_time="08:00", recurring=False)
    midday_task = Task(title="Morning Walk", duration=30, priority=5, due_time="09:00", recurring=False)

    scheduler = Scheduler(tasks=[evening_task, morning_task, midday_task])

    sorted_tasks = scheduler.sort_by_time()

    assert [task.due_time for task in sorted_tasks] == ["08:00", "09:00", "17:00"]


def test_sort_by_time_does_not_mutate_original_task_order():
    task_a = Task(title="Task A", duration=10, priority=1, due_time="18:00", recurring=False)
    task_b = Task(title="Task B", duration=10, priority=1, due_time="06:00", recurring=False)

    scheduler = Scheduler(tasks=[task_a, task_b])
    scheduler.sort_by_time()

    # sort_by_time returns a new sorted list; scheduler.tasks stays untouched.
    assert scheduler.tasks == [task_a, task_b]


def test_sort_by_time_on_empty_scheduler_returns_empty_list():
    scheduler = Scheduler(tasks=[])

    assert scheduler.sort_by_time() == []


# --- Recurring task logic ------------------------------------------------


def test_recurring_task_creates_next_occurrence_for_following_day():
    original_due_date = date(2026, 1, 1)
    task = Task(
        title="Give Medication",
        duration=5,
        priority=5,
        due_time="19:30",
        recurring=True,
        recurrence="daily",
        due_date=original_due_date,
    )

    next_task = task.mark_complete()

    # A new task is created for the following day with the same details.
    assert next_task is not None
    assert next_task.due_date == original_due_date + timedelta(days=1)
    assert next_task.title == task.title
    assert next_task.due_time == task.due_time
    assert next_task.completed is False


def test_recurring_task_original_remains_completed_after_recurrence():
    task = Task(
        title="Give Medication",
        duration=5,
        priority=5,
        due_time="19:30",
        recurring=True,
        recurrence="daily",
    )

    task.mark_complete()

    # The original task stays in place as completed history, not overwritten.
    assert task.completed is True


def test_non_recurring_task_has_no_next_occurrence():
    task = Task(title="Vet Visit", duration=60, priority=4, due_time="14:00", recurring=False)

    next_task = task.mark_complete()

    assert next_task is None
    assert task.completed is True


# --- Conflict detection ---------------------------------------------------


def test_detect_conflicts_warns_about_tasks_at_same_time():
    task_a = Task(title="Morning Walk", duration=30, priority=5, due_time="09:00", recurring=False)
    task_b = Task(title="Grooming", duration=15, priority=2, due_time="09:00", recurring=False)

    scheduler = Scheduler(tasks=[task_a, task_b])

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    # The warning should call out the conflicting time or the task names.
    assert "09:00" in warnings[0]
    assert "Morning Walk" in warnings[0]
    assert "Grooming" in warnings[0]


def test_detect_conflicts_returns_empty_when_no_tasks_overlap():
    task_a = Task(title="Feed Buddy", duration=10, priority=3, due_time="08:00", recurring=False)
    task_b = Task(title="Playtime", duration=20, priority=2, due_time="17:00", recurring=False)

    scheduler = Scheduler(tasks=[task_a, task_b])

    assert scheduler.detect_conflicts() == []
