📝 To-Do List (Python CLI Project)
📌 Project Description

This is a simple To-Do List application built using Python.
It runs in the terminal and allows users to manage their daily tasks.

The program is menu-driven and supports basic operations like:

Adding tasks
Viewing tasks
Updating tasks
Deleting tasks
🎯 Features
➕ Add new tasks
👀 View all tasks
✏️ Update existing tasks
❌ Delete tasks
🖥️ Clean terminal interface
🧠 How It Works

The program follows a simple logic:

1. Data Storage
.All tasks are stored in a list
.tasks = []
.Each task is stored as a string inside the list
2. Functions Breakdown
🔹 clear()
.Clears the terminal screen
.Works on both Windows and Linux
🔹 add_task(tasks)
.Takes input from user
.Adds the task to the list using:
tasks.append(task)
🔹 view_tasks(tasks)
.Displays all tasks
.Uses a loop with numbering:
for i, task in enumerate(tasks, start=1):
🔹 update_task(tasks)
.Lets user modify an existing task
.Replaces the task using:
tasks[index] = new_value
🔹 delete_task(tasks)
.Removes a task from the list
.Uses:
tasks.pop(index)
3. Main Program Loop
.Runs continuously using:
while True:
.Displays menu options
.Calls functions based on user input
⚙️ Technologies Used
.Python (Core concepts)
.Lists
.Functions
.Loops
.Conditional statements
.Exception handling
🚀 How to Run
.Install Python
.Save the file as todo.py
.Run in terminal:
python todo.py
⚠️ Limitations
.Tasks are stored in memory (RAM)
.Data will be lost when program is closed
📚 Learning Outcome

This project helps in understanding:

.How to store multiple values using lists
.How to build menu-driven programs
.Basic CRUD operations (Create, Read, Update, Delete)

🙌 Author:
Created by: Shoaib Bhatti
