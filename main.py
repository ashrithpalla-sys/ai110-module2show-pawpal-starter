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


def main() -> None:
    # Create an owner.
    owner = Owner(name="Alex", available_time=120, preferences={"morning_first": True})

    # Create pets and add them to the owner.
    buddy = Pet(name="Buddy", species="Dog", age=4)
    luna = Pet(name="Luna", species="Cat", age=2)
    owner.add_pet(buddy)
    owner.add_pet(luna)

    # Create tasks with varying durations, priorities, and due times.
    feed_buddy = Task(title="Feed Buddy", duration=10, priority=3, due_time="08:00", recurring=True)
    morning_walk = Task(title="Morning Walk", duration=30, priority=5, due_time="09:00", recurring=True)
    playtime = Task(title="Playtime", duration=20, priority=2, due_time="17:00", recurring=False)
    give_medication = Task(title="Give Medication", duration=5, priority=5, due_time="19:30", recurring=True)

    # Assign tasks to the appropriate pets.
    buddy.add_task(feed_buddy)
    buddy.add_task(morning_walk)
    luna.add_task(playtime)
    luna.add_task(give_medication)

    # Display all assigned tasks grouped by pet.
    print_todays_schedule(owner)

    # Run the actual Scheduler logic over every task and available time.
    scheduler = Scheduler(tasks=owner.get_all_tasks(), available_time=owner.available_time)
    scheduler.generate_daily_plan()
    print("\n" + scheduler.explain_schedule())


if __name__ == "__main__":
    main()
