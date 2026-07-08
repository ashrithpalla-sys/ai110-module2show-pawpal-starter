"""
PawPal+ CLI demo.

A temporary command-line script that exercises the Owner, Pet, Task, and
Scheduler classes from pawpal_system.py to verify the object relationships
work end to end.
"""

from datetime import datetime

from pawpal_system import Owner, Pet, Task, Scheduler


def format_time(due_time: str) -> str:
    """Convert a 24-hour "HH:MM" string into a friendly "H:MM AM/PM" string."""
    parsed = datetime.strptime(due_time, "%H:%M")
    return parsed.strftime("%I:%M %p").lstrip("0")


def print_todays_schedule(owner: Owner) -> None:
    """Print each pet's assigned tasks under a formatted header."""
    print("=" * 33)
    print("        Today's Schedule")
    print("=" * 33)
    print(f"Owner: {owner.name}")
    print(f"Available Time: {owner.available_time} minutes")

    for pet in owner.pets:
        print(f"\nPet: {pet.name}")
        for task in pet.get_tasks():
            print(f"- {task.title} ({format_time(task.due_time)}) | "
                  f"Priority: {task.priority} | {task.duration} min")

    print("\n" + "=" * 33)


def print_task_list(heading: str, tasks: list[Task]) -> None:
    """Print a labeled list of tasks with pet, time, priority, and status."""
    print(f"\n{heading}")
    if not tasks:
        print("  (none)")
        return
    for task in tasks:
        status = "done" if task.completed else "pending"
        print(f"  - {task.title} ({task.pet_name}) at {format_time(task.due_time)} "
              f"| Priority: {task.priority} | {status}")


def main() -> None:
    # Create an owner.
    owner = Owner(name="Alex", available_time=120, preferences={"morning_first": True})

    # Create pets and add them to the owner.
    buddy = Pet(name="Buddy", species="Dog", age=4)
    luna = Pet(name="Luna", species="Cat", age=2)
    owner.add_pet(buddy)
    owner.add_pet(luna)

    # Create tasks out of chronological order to show that sort_by_time()
    # reorders them regardless of creation order.
    give_medication = Task(
        title="Give Medication", duration=5, priority=5, due_time="19:30",
        recurring=True, recurrence="weekly",
    )
    playtime = Task(title="Playtime", duration=20, priority=2, due_time="17:00", recurring=False, completed=True)
    feed_buddy = Task(title="Feed Buddy", duration=10, priority=3, due_time="08:00", recurring=True, completed=True)
    morning_walk = Task(
        title="Morning Walk", duration=30, priority=5, due_time="09:00",
        recurring=True, recurrence="daily",
    )
    # Same due_time as Morning Walk, but for a different pet — intentional
    # collision to demonstrate cross-pet conflict detection.
    grooming = Task(title="Grooming", duration=15, priority=2, due_time="09:00", recurring=False)

    # Assign tasks out of chronological order within each pet too, so the
    # "original order" below isn't accidentally already sorted.
    buddy.add_task(morning_walk)
    buddy.add_task(feed_buddy)
    luna.add_task(give_medication)
    luna.add_task(playtime)
    luna.add_task(grooming)

    # Display all assigned tasks grouped by pet.
    print_todays_schedule(owner)

    # Run the actual Scheduler logic over every task and available time.
    scheduler = Scheduler(tasks=owner.get_all_tasks(), available_time=owner.available_time)

    print_task_list("Original order (as created):", scheduler.tasks)
    print_task_list("Sorted by due_time:", scheduler.sort_by_time())
    print_task_list("Buddy's tasks only:", scheduler.filter_tasks(pet_name="Buddy"))
    print_task_list("Completed tasks:", scheduler.filter_tasks(completed=True))
    print_task_list("Incomplete tasks:", scheduler.filter_tasks(completed=False))

    # Demonstrate conflict detection: Morning Walk (Buddy) and Grooming (Luna)
    # were both intentionally scheduled for 09:00.
    print("\n" + "=" * 33)
    print("   Conflict Detection Demo")
    print("=" * 33)
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            print(f"  ! {warning}")
    else:
        print("  No conflicts found.")

    scheduler.generate_daily_plan()
    print("\n" + scheduler.explain_schedule())

    # Demonstrate recurring tasks: completing a "daily" task spawns tomorrow's
    # occurrence, while the completed task stays in the scheduler as history.
    print("\n" + "=" * 33)
    print("   Recurring Task Demo")
    print("=" * 33)
    print(f"Before: {morning_walk.title} due {morning_walk.due_date}, completed={morning_walk.completed}")

    next_walk = scheduler.complete_task(morning_walk)
    buddy.add_task(next_walk)  # keep Buddy's own task list in sync too

    print(f"After:  {morning_walk.title} due {morning_walk.due_date}, completed={morning_walk.completed} (kept in history)")
    print(f"Spawned next occurrence: {next_walk.title} due {next_walk.due_date}, completed={next_walk.completed}")
    print(f"Scheduler now holds {len(scheduler.tasks)} tasks (was {len(scheduler.tasks) - 1} before completion).")


if __name__ == "__main__":
    main()
