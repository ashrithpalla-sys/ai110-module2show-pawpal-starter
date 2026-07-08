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
The Owner class represents the pet owner and stores information such as their name, available time, preferences, and the pets they own. It is responsible for managing pets and requesting a daily schedule. The Pet class represents an individual pet. It stores basic information like the pet's name, species, age, and a list of care tasks. Its responsibility is to organize and manage the tasks associated with that specific pet.The Task class represents a single pet care activity, such as feeding, walking, medication, grooming, or playtime. Each task stores details including its duration, priority, due time, whether it is recurring, and whether it has been completed. It also provides methods for updating task information and checking for scheduling conflicts. The Scheduler class contains the application's scheduling logic. It is responsible for prioritizing tasks, detecting conflicts, generating an optimized daily care plan based on the owner's available time, and explaining why tasks were scheduled in a particular order. This design separates responsibilities across classes, making the system modular, easier to maintain, and easier to extend with additional scheduling features in the future.

- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
