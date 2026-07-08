"""Pytest tests for the core PawPal+ classes in pawpal_system.py."""

from pawpal_system import Pet, Task


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
