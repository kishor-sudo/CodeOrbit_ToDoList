# CodeOrbit To-Do List CLI App

A beginner-friendly **command-line To-Do List application built using Python** as part of my **CodeOrbit Tech Python Programming Internship**.

## 📌 Project Overview

This project is a simple task management application that allows users to create, view, complete, and remove tasks directly from the command line.

The application also uses a **JSON file** to save tasks so that they can be loaded again when the program is restarted.

## ✨ Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Remove tasks
* Clear all tasks
* Numbered task display
* Input validation
* Error handling
* Save tasks to a JSON file
* Load saved tasks when the program starts
* Menu-driven command-line interface

## 🛠️ Technologies Used

* **Python 3**
* `json` — for saving and loading task data
* `os` — for checking whether the task file exists

No external libraries are required.

## 🖥️ Application Menu

```text
========================================
          TASK MANAGER
========================================

1. Add Task
2. View Tasks
3. Complete Task
4. Remove Task
5. Clear All Tasks
6. Exit
```

## 📋 How It Works

### 1. Add Task

The user enters a task description.

Example:

```text
Enter task: Study Python
```

The task is added with a **Pending** status.

### 2. View Tasks

The application displays all tasks with their task number and status.

Example:

```text
--- Your Tasks ---

1. Study Python [Pending]
2. Complete internship [Completed]
3. Read documentation [Pending]
```

### 3. Complete Task

The user selects a task number to mark it as completed.

Example:

```text
Enter task number to complete: 1

Task 'Study Python' marked as completed!
```

The status changes from:

```text
[Pending]
```

to:

```text
[Completed]
```

### 4. Remove Task

The user can remove a task by entering its task number.

Example:

```text
Enter task number to remove: 2

Task 'Complete internship' removed successfully!
```

### 5. Clear All Tasks

The application asks for confirmation before deleting all tasks.

```text
Are you sure you want to clear all tasks? (y/n):
```

This helps prevent accidental deletion.

### 6. File Persistence

Tasks are stored in:

```text
tasks.json
```

When the program starts, previously saved tasks are loaded automatically.

Example JSON structure:

```json
[
  {
    "title": "Study Python",
    "completed": false
  },
  {
    "title": "Finish internship",
    "completed": true
  }
]
```

## ⚠️ Error Handling

The program handles common invalid inputs without crashing.

### Invalid menu choice

```text
Error: Please choose a valid option from 1 to 6.
```

### Invalid task number

```text
Error: Please enter a valid task number.
```

### Task does not exist

```text
Error: That task does not exist.
```

### Empty task

```text
Error: Task cannot be empty.
```

## 🧠 Python Concepts Learned

This project helped me practice:

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Input validation
* Exception handling
* File handling
* JSON
* Basic CRUD operations
* Program organization

## ▶️ How to Run

### 1. Install Python

Make sure **Python 3** is installed on your system.

### 2. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 3. Open the project folder

```bash
cd CodeOrbit_ToDoList
```

### 4. Run the application

```bash
python todo_list.py
```

## 📁 Project Structure

```text
CodeOrbit_ToDoList/
│
├── todo_list.py
├── tasks.json
└── README.md
```

> `tasks.json` is created/updated by the program to store task information.

## 🧪 Testing

The application was tested for:

* Adding a single task
* Adding multiple tasks
* Viewing tasks
* Completing tasks
* Removing tasks
* Clearing all tasks
* Invalid menu choices
* Invalid task numbers
* Non-existent task numbers
* Empty task input
* Saving tasks
* Loading tasks after restarting the program

## 🎯 Internship Task

This project was completed as **Task 2 — To-Do List CLI App** for the **CodeOrbit Tech Python Programming Internship**.

The application satisfies the required functionality of adding, viewing, and removing tasks using Python, with additional improvements such as task completion and file persistence.

## 👨‍💻 Author

**Kishor B**

GitHub: <your-github-profile-link>
