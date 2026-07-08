import os

# Function to clear screen (it helps to code works on Windows & Linux)
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------ ADD TASK -------------------
def add_task(tasks):
    clear()  # clear screen before taking input
    
    # asking user to enter a new task
    task = input("Enter new task: ")
    
    # adding task to list
    tasks.append(task)
    
    print("Task added successfully!\n")


# ------------------- VIEW TASKS ------------------
def view_tasks(tasks):
    clear()
    print("==== YOUR TASKS ====\n")

    # if list is empty
    if not tasks:
        print("No tasks available!\n")
        return

    # display all tasks with numbering
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
    print()


# ------------------ UPDATE TASK -------------------
def update_task(tasks):
    # first show all tasks
    view_tasks(tasks)

    # if no tasks, exit function
    if not tasks:
        return

    try:
        # asking user which task to update
        num = int(input("Enter task number to update: "))
        
        # checking if number is valid
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ")
            
            # replacing old task with new one
            tasks[num - 1] = new_task
            
            print("Task updated successfully!\n")
        else:
            print("Invalid number!\n")

    except ValueError:
        # if user enters non-number
        print("Enter a valid number!\n")


# ------------------ DELETE TASK -----------------
def delete_task(tasks):
    # show tasks before deleting
    view_tasks(tasks)

    if not tasks:
        return

    try:
        # asking which task to delete
        num = int(input("Enter task number to delete: "))
        
        # validating input
        if 1 <= num <= len(tasks):
            # removing task from list
            removed = tasks.pop(num - 1)
            
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid number!\n")

    except ValueError:
        print("Enter a valid number!\n")


# ------------------- MAIN PROGRAM ----------------

tasks = []  # this list will store all tasks

while True:
    print("==== TO-DO LIST ====\n")
    
    # menu options
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    # taking user choice
    choice = input("Choose option: ")

    # checking user choice
    if choice == '1':
        add_task(tasks)

    elif choice == '2':
        view_tasks(tasks)

    elif choice == '3':
        update_task(tasks)

    elif choice == '4':
        delete_task(tasks)

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again!\n")