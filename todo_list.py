"""
To-Do List CLI App - CodeOrbit Tech Internship
A simple task manager with file persistence
"""

import json
import os


# ============================================
# FILE HANDLING FUNCTIONS
# ============================================

def load_tasks(filename="tasks.json"):
    """
    Load tasks from a JSON file.
    If the file doesn't exist, return an empty list.
    """
    # Check if the file exists
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is corrupted or empty, start fresh
            return []
    else:
        # No file yet, start with empty list
        return []


def save_tasks(tasks, filename="tasks.json"):
    """
    Save tasks to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=2)


# ============================================
# CORE TASK OPERATIONS
# ============================================

def add_task(tasks):
    """
    Add a new task to the list.
    """
    print("\n--- Add New Task ---")
    
    # Get task description
    task_title = input("Enter task: ").strip()
    
    # Validate: task cannot be empty
    if not task_title:
        print("Error: Task cannot be empty.")
        return False
    
    # Add the task
    tasks.append({
        "title": task_title,
        "completed": False
    })
    
    print(f"Task '{task_title}' added successfully!")
    return True


def view_tasks(tasks):
    """
    Display all tasks with their status.
    """
    print("\n--- Your Tasks ---")
    
    # Check if there are any tasks
    if not tasks:
        print("No tasks found. Add a task first!")
        return
    
    # Display each task with a number
    for i, task in enumerate(tasks, 1):
        # Determine status symbol
        if task["completed"]:
            status = "[Completed]"
        else:
            status = "[Pending]"
        
        print(f"{i}. {task['title']} {status}")


def complete_task(tasks):
    """
    Mark a task as completed.
    """
    # First show current tasks
    view_tasks(tasks)
    
    # Check if there are tasks
    if not tasks:
        return
    
    print("\n--- Complete Task ---")
    
    # Get task number
    try:
        task_num = int(input("Enter task number to complete: "))
        
        # Check if the task number is valid
        if 1 <= task_num <= len(tasks):
            # Mark as completed
            tasks[task_num - 1]["completed"] = True
            task_title = tasks[task_num - 1]["title"]
            print(f"Task '{task_title}' marked as completed!")
        else:
            print("Error: That task does not exist.")
    except ValueError:
        print("Error: Please enter a valid task number.")


def remove_task(tasks):
    """
    Remove a task from the list.
    """
    # First show current tasks
    view_tasks(tasks)
    
    # Check if there are tasks
    if not tasks:
        return
    
    print("\n--- Remove Task ---")
    
    # Get task number
    try:
        task_num = int(input("Enter task number to remove: "))
        
        # Check if the task number is valid
        if 1 <= task_num <= len(tasks):
            # Get the task title before removing
            task_title = tasks[task_num - 1]["title"]
            
            # Remove the task
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{task_title}' removed successfully!")
        else:
            print("Error: That task does not exist.")
    except ValueError:
        print("Error: Please enter a valid task number.")


def clear_tasks(tasks):
    """
    Clear all tasks after confirmation.
    """
    print("\n--- Clear All Tasks ---")
    
    # Check if there are tasks
    if not tasks:
        print("No tasks to clear.")
        return
    
    # Confirm with user
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes']:
        tasks.clear()
        print("All tasks have been cleared!")
    else:
        print("Operation cancelled.")


# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_menu():
    """
    Display the main menu.
    """
    print("\n" + "=" * 40)
    print("          TASK MANAGER")
    print("=" * 40)
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Clear All Tasks")
    print("6. Exit")
    print("-" * 40)


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """
    Main program loop.
    """
    print("\n" + "=" * 40)
    print("   WELCOME TO TASK MANAGER")
    print("=" * 40)
    
    # Load existing tasks
    tasks = load_tasks()
    
    # Show how many tasks were loaded
    if tasks:
        print(f"Loaded {len(tasks)} task(s) from file.")
    else:
        print("Starting with no tasks.")
    
    # Main loop - runs until user exits
    while True:
        display_menu()
        
        choice = input("Enter your choice: ").strip()
        
        # Process user choice
        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)  # Save after adding
        
        elif choice == '2':
            view_tasks(tasks)
        
        elif choice == '3':
            complete_task(tasks)
            save_tasks(tasks)  # Save after completing
        
        elif choice == '4':
            remove_task(tasks)
            save_tasks(tasks)  # Save after removing
        
        elif choice == '5':
            clear_tasks(tasks)
            save_tasks(tasks)  # Save after clearing
        
        elif choice == '6':
            print("\n" + "=" * 40)
            print("Thank you for using Task Manager!")
            print("Goodbye!")
            print("=" * 40)
            break
        
        else:
            print("Error: Please choose a valid option from 1 to 6.")


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()