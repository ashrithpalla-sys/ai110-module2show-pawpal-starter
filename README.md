# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

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
Running pytest with args: ['-p', 'vscode_pytest', '--rootdir=/Users/ashrithpalla/Desktop/cp-AI/ai110-module2show-pawpal-starter', '/Users/ashrithpalla/Desktop/cp-AI/ai110-module2show-pawpal-starter/tests/test_pawpal.py::test_mark_complete', '/Users/ashrithpalla/Desktop/cp-AI/ai110-module2show-pawpal-starter/tests/test_pawpal.py::test_add_task_to_pet']
============================= test session starts ==============================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/ashrithpalla/Desktop/cp-AI/ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 2 items

tests/test_pawpal.py ..                                                  [100%]

============================== 2 passed in 0.01s ===============================
Finished running tests!

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Sort by time | `Scheduler.sort_by_time()` | Returns all tasks ordered chronologically by `due_time`, independent of priority — useful for a simple "what's my day look like" view. |
| Filter by pet / status | `Scheduler.filter_tasks()` | Returns tasks matching an optional `pet_name` and/or `completed` flag, so callers can ask for one pet's tasks, only completed tasks, or both, without writing ad-hoc list comprehensions. |
| Conflict detection | `Scheduler.detect_conflicts()` | Scans all tasks for pairs sharing the exact same `due_time` and returns a list of human-readable warning strings (e.g. `Conflict: "Morning Walk" and "Grooming" are both due at 09:00.`) rather than raising — works across any pets sharing the scheduler. |
| Recurring tasks | `Task.mark_complete()`, `Task.create_next_occurrence()`, `Scheduler.complete_task()` | Completing a task with a `recurrence` of `"daily"` or `"weekly"` automatically generates its next occurrence with the `due_date` advanced by one or seven days. The completed task stays in place as history; `Scheduler.complete_task()` adds the new occurrence back into the scheduler and returns it. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
