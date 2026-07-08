# PawPal+ Project Reflection

## 1. System Design
Add and manage pet care tasks
    The owner can create, edit, or remove tasks such as feeding, walking, medication, grooming, or playtime. Each task includes information like duration, priority, due time, and whether it repeats daily.
Generate a daily care schedule
    The owner can request a daily plan, and the system automatically selects and orders tasks based on available time, task priority, deadlines, and owner preferences. If there are scheduling conflicts, the system prioritizes the most important tasks.
View today's schedule and explanations
    The owner can view an organized list of today's planned tasks along with an explanation of why each task appears in that order (for example, "Medication scheduled first because it is high priority and due before noon"). This helps the owner understand the scheduling decisions and make adjustments if needed.

**a. Initial design**

- Briefly describe your initial UML design.
For my initial UML design, I included four main classes: Owner, Pet, Task, and Scheduler.

- What classes did you include, and what responsibilities did you assign to each?
The Owner class represents the pet owner and stores information such as their name, available time, preferences, and the pets they own. It is responsible for managing pets and requesting a daily schedule. The Pet class represents an individual pet. It stores basic information like the pet's name, species, age, and a list of care tasks. Its responsibility is to organize and manage the tasks associated with that specific pet.The Task class represents a single pet care activity, such as feeding, walking, medication, grooming, or playtime. Each task stores details including its duration, priority, due time, whether it is recurring, and whether it has been completed. It also provides methods for updating task information and checking for scheduling conflicts. The Scheduler class contains the application's scheduling logic. It is responsible for prioritizing tasks, detecting conflicts, generating an optimized daily care plan based on the owner's available time, and explaining why tasks were scheduled in a particular order. This design separates responsibilities across classes, making the system modular, easier to maintain, and easier to extend with additional scheduling features in the future.

**b. Design changes**

- Did your design change during implementation?
Yes
- If yes, describe at least one change and why you made it.
My initial design included four main classes: Owner, Pet, Task, and Scheduler. During implementation, I expanded the responsibilities of the Scheduler class to include more algorithmic features such as sorting tasks by time, filtering tasks, detecting conflicts, and handling recurring tasks. I made this change because the original design focused mostly on storing information, but the Scheduler needed a clearer role as the part of the system responsible for planning and decision-making. Separating this logic from the Pet and Task classes kept the system more modular and easier to maintain.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
The scheduler considers several constraints when organizing tasks:
    - Task due time
    - Task priority level
    - Owner available time
    - Task completion status
    - Recurring task frequency

- How did you decide which constraints mattered most?
I decided that due time and priority should matter most because missing time-sensitive tasks, such as medication, could negatively affect the pet's health. Lower-priority tasks like enrichment or grooming can be scheduled after more urgent responsibilities.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is that conflict detection only checks whether two tasks have the exact same scheduled time instead of checking for overlapping durations.
- Why is that tradeoff reasonable for this scenario?
This approach is reasonable because it keeps the scheduling algorithm simple and predictable while still catching obvious scheduling mistakes. A more advanced system could compare task start and end times, but that would add additional complexity that was unnecessary for this project.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI throughout the project as a design and development assistant. I used it to brainstorm class structures, generate UML diagrams, create initial class skeletons, debug issues, design pytest tests, and improve documentation.

- What kinds of prompts or questions were most helpful?
The most helpful prompts were ones that asked AI to review specific parts of my implementation, such as asking for edge cases to test, suggestions for improving scheduling algorithms, and explanations of Python concepts like dataclasses, sorting with lambda functions, and timedelta.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One time I did not accept an AI suggestion immediately was when it suggested a more compact implementation for scheduling logic. Although the solution was shorter, I kept a slightly longer version because it was easier to understand, debug, and explain.

- How did you evaluate or verify what the AI suggested?
I evaluated the suggestion by comparing readability, maintainability, and whether the implementation matched the goals of the project. I also verified any changes by running tests and checking the behavior through my CLI demo.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested several important behaviors:
    Creating pets and adding tasks
    Marking tasks as complete
    Sorting tasks chronologically
    Creating new occurrences for recurring tasks
    Detecting scheduling conflicts

- Why were these tests important?
These tests were important because they verified both the basic functionality of my classes and the more complex scheduling algorithms. Testing ensured that changes to one part of the system did not break another part.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am confident that my scheduler works correctly for the scenarios it was designed to handle. The automated tests verify the main behaviors, and the CLI demo helped confirm that the system works from a user's perspective.

- What edge cases would you test next if you had more time?
If I had more time, I would test additional edge cases such as:
    Tasks with missing or invalid times
    Multiple pets with many overlapping tasks
    Recurring tasks across different dates
    Schedules where the available time is less than the total task duration
    Tasks with equal priorities and different deadlines

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with how the project evolved from a simple object model into a functional scheduling system. The separation between the backend logic and Streamlit interface made the project easier to expand, and the Scheduler class provided a clear place for algorithmic improvements.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduling algorithm by considering task durations and automatically rearranging tasks to prevent overlapping schedules. I would also add more user customization options, such as preferred walking times or different scheduling priorities for different pets.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
The biggest lesson I learned is that designing a system requires thinking about responsibilities before writing code. AI tools were valuable for generating ideas and accelerating development, but I still needed to make design decisions, evaluate suggestions, and verify that the final implementation matched the intended behavior.
