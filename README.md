# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## Features

- **Pet management** — Owners can add multiple pets (`Pet`), each with a name, species, and age, and every pet keeps its own list of care tasks.
- **Task management** — Care tasks (`Task`) capture a title, duration, priority, due time, and optional recurrence, and can be added to or removed from a pet, marked complete, or have their priority updated.
- **Schedule generation** — `Scheduler.generate_daily_plan()` greedily builds a day's plan by priority, skipping tasks that are already completed, don't fit in the owner's remaining available time, or conflict with an already-scheduled task — and `explain_schedule()` produces a human-readable summary of what was scheduled and why.
- **Task sorting by time** — `Scheduler.sort_by_time()` returns all tasks ordered chronologically by due time, independent of priority, for an at-a-glance view of the day.
- **Task filtering** — `Scheduler.filter_tasks()` filters tasks by pet and/or completion status, so callers can view one pet's tasks, only completed/incomplete tasks, or any combination.
- **Conflict detection** — `Scheduler.detect_conflicts()` scans all tasks across every pet and returns clear warnings for any that share the same due time.
- **Recurring daily/weekly tasks** — Completing a task with `"daily"` or `"weekly"` recurrence automatically generates its next occurrence with the due date advanced accordingly, while the completed task is kept in place as history.
- **CLI demo** — `main.py` exercises the full object model end to end (adding pets/tasks, sorting, filtering, conflict detection, schedule generation, and recurrence) as a quick way to see the backend logic run without the UI.
- **Streamlit interface** — `app.py` provides an interactive UI to add owners, pets, and tasks; filter and sort tasks; complete tasks (including spawning recurring occurrences); view conflict warnings; and generate and display the daily schedule.
- **Automated pytest testing** — A pytest suite (`tests/test_pawpal.py`) covers the core scheduling behaviors, including task completion, sorting, recurring task creation, and conflict detection.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

=================================
        Today's Schedule
=================================
Owner: Alex
Available Time: 120 minutes

Pet: Buddy
- Feed Buddy (8:00 AM) | Priority: 3 | 10 min
- Morning Walk (9:00 AM) | Priority: 5 | 30 min

Pet: Luna
- Playtime (5:00 PM) | Priority: 2 | 20 min
- Give Medication (7:30 PM) | Priority: 5 | 5 min

=================================

Daily Schedule Explanation:

Scheduled tasks (in order):
  1. Morning Walk — priority 5, due 09:00, 30 min
  2. Give Medication — priority 5, due 19:30, 5 min
  3. Feed Buddy — priority 3, due 08:00, 10 min
  4. Playtime — priority 2, due 17:00, 20 min

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```
============================= test session starts ==============================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/ashrithpalla/Desktop/cp-AI/ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 10 items

tests/test_pawpal.py ..........                                          [100%]

============================== 10 passed in 0.01s ==============================
Finished running tests!

Test Coverage

The automated tests verify:

Task completion updates the task's status correctly.
  Pets can successfully add and store tasks.
  Tasks are sorted into chronological order.
  Daily recurring tasks generate the next occurrence automatically.
  Scheduling conflicts are detected when multiple tasks share the same scheduled time.
Confidence Level: 4/5 stars --> The test suite covers the application's most important scheduling behaviors, including sorting, recurring tasks, and conflict detection. Additional tests for more complex scheduling scenarios and user interactions would further improve reliability.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Sort by time | `Scheduler.sort_by_time()` | Returns all tasks ordered chronologically by `due_time`, independent of priority — useful for a simple "what's my day look like" view. |
| Filter by pet / status | `Scheduler.filter_tasks()` | Returns tasks matching an optional `pet_name` and/or `completed` flag, so callers can ask for one pet's tasks, only completed tasks, or both, without writing ad-hoc list comprehensions. |
| Conflict detection | `Scheduler.detect_conflicts()` | Scans all tasks for pairs sharing the exact same `due_time` and returns a list of human-readable warning strings (e.g. `Conflict: "Morning Walk" and "Grooming" are both due at 09:00.`) rather than raising — works across any pets sharing the scheduler. |
| Recurring tasks | `Task.mark_complete()`, `Task.create_next_occurrence()`, `Scheduler.complete_task()` | Completing a task with a `recurrence` of `"daily"` or `"weekly"` automatically generates its next occurrence with the `due_date` advanced by one or seven days. The completed task stays in place as history; `Scheduler.complete_task()` adds the new occurrence back into the scheduler and returns it. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. The user starts by entering basic owner information and creating a profile for their pets. Each pet is stored in the system and can have its own set of care tasks.
2. The user adds pet care tasks such as feeding, walks, medication, grooming, or enrichment activities. Each task includes details like duration, priority, scheduled time, and whether it is recurring.
3. The user views the generated daily schedule. The Scheduler organizes tasks automatically by time and uses the owner's available time to create a manageable care plan.
4. The app highlights important scheduling information, including task priorities, completed tasks, and any conflicts detected when multiple tasks are scheduled for the same time.
5. The user can filter tasks by pet or completion status to quickly find specific activities and manage their daily routine.
6. When a recurring task, such as a daily medication reminder, is completed, the system automatically creates the next occurrence so the pet's routine continues without manual re-entry.
7. The CLI demo (main.py) demonstrates the backend functionality by creating pets and tasks, generating schedules, sorting tasks, and displaying conflict warnings directly in the terminal.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
