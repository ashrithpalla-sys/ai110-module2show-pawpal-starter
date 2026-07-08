from datetime import time

import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner")
owner_name = st.text_input("Owner name", value="Jordan")

# Streamlit reruns this whole script top-to-bottom on every interaction, so a
# plain local variable would be recreated (and lose its data) each time. Storing
# the Owner in st.session_state keeps the same object alive across reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, available_time=120)
owner = st.session_state.owner
owner.name = owner_name

PRIORITY_LABELS = {"low": 1, "medium": 3, "high": 5}

st.subheader("Add a Pet")
with st.form("add_pet_form"):
    new_pet_name = st.text_input("Pet name", value="Mochi")
    new_pet_species = st.selectbox("Species", ["dog", "cat", "other"])
    new_pet_age = st.number_input("Age", min_value=0, max_value=30, value=1)
    pet_submitted = st.form_submit_button("Add Pet")

if pet_submitted:
    owner.add_pet(Pet(name=new_pet_name, species=new_pet_species, age=int(new_pet_age)))
    st.success(f"Added pet: {new_pet_name}")

st.subheader("Add a Task")
if owner.pets:
    with st.form("add_task_form"):
        target_pet_name = st.selectbox("Pet", [pet.name for pet in owner.pets])
        task_title = st.text_input("Task title", value="Morning walk")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        priority_label = st.selectbox("Priority", list(PRIORITY_LABELS), index=2)
        due_time = st.time_input("Due time", value=time(8, 0))
        recurring = st.checkbox("Recurring")
        task_submitted = st.form_submit_button("Add Task")

    if task_submitted:
        target_pet = next(pet for pet in owner.pets if pet.name == target_pet_name)
        target_pet.add_task(
            Task(
                title=task_title,
                duration=int(duration),
                priority=PRIORITY_LABELS[priority_label],
                due_time=due_time.strftime("%H:%M"),
                recurring=recurring,
            )
        )
        st.success(f"Added task '{task_title}' to {target_pet_name}")
else:
    st.info("Add a pet first before creating tasks.")

st.markdown("### Your Pets & Tasks")
if owner.pets:
    for pet in owner.pets:
        with st.expander(f"{pet.name} ({pet.species}, age {pet.age})", expanded=True):
            tasks = pet.get_tasks()
            if tasks:
                st.table(
                    [
                        {
                            "Title": task.title,
                            "Duration (min)": task.duration,
                            "Priority": task.priority,
                            "Due": task.due_time,
                            "Recurring": task.recurring,
                            "Completed": task.completed,
                        }
                        for task in tasks
                    ]
                )
            else:
                st.caption("No tasks yet.")
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
available_time = st.number_input(
    "Available time today (minutes)", min_value=0, max_value=1440, value=owner.available_time
)
owner.available_time = int(available_time)

if st.button("Generate schedule"):
    scheduler = owner.generate_schedule()
    st.code(scheduler.explain_schedule())
