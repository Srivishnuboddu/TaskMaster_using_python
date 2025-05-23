# TaskMaster: Your Personal Task Manager

#### Video Demo: (https://youtu.be/7U0NFQT6CIs)
#### Description:

TaskMaster is a simple yet powerful To-Do List application designed to help users manage their daily tasks efficiently. This application allows users to add, view, and remove tasks seamlessly through a command-line interface. Implemented in Python, TaskMaster offers a lightweight and easy-to-use solution for personal task management.

## Features

- **Add Task**: Easily add new tasks to your to-do list.
- **View Tasks**: View all tasks currently in your to-do list.
- **Remove Task**: Remove tasks that have been completed or are no longer needed.

## Project Structure

- **project.py**: This is the main file containing the core functionality of the application. It includes the following functions:
  - `main()`: The main function that runs the application.
  - `view_tasks()`: Function to display the current tasks.
  - `add_task(task)`: Function to add a new task.
  - `remove_task(task_idx)`: Function to remove a task by its index.
  - `get_tasks()`: Function to retrieve tasks from the tasks.txt file.
  - `save_tasks(tasks)`: Function to save tasks to the tasks.txt file.

- **test_project.py**: This file contains tests for the functions in `project.py` using pytest. It includes tests for:
  - `test_get_tasks()`: Tests the retrieval of tasks.
  - `test_save_tasks()`: Tests the saving of tasks.
  - `test_add_task()`: Tests adding a new task.
  - `test_remove_task()`: Tests removing a task.

## Design Choices

### File-based Storage
The decision to use a plain text file (tasks.txt) for storing tasks was made to keep the project simple and avoid the complexity of databases. This approach allows for easy reading and writing of tasks.

### Command-line Interface
A command-line interface (CLI) was chosen for its simplicity and ease of implementation. This makes the application accessible to users familiar with command-line tools and allows for quick interactions with the to-do list.

### Function-Based Structure
The application is structured using functions, making the code modular and easier to test. Each function handles a specific part of the task management process, allowing for clear and maintainable code.

## Usage

To use TaskMaster, follow these steps:

1. **Clone the Repository**:
    ```bash
    (# go to my project folder for project code)
    cd taskmaster
    ```

2. **Install Dependencies**:
    Make sure you have Python installed. Then install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    Execute the `project.py` file to start the application:
    ```bash
    python project.py
    ```

4. **Interact with the Application**:
    Use the menu options to add, view, or remove tasks.

## Running Tests

To ensure the application functions correctly, you can run the tests provided in `test_project.py` using pytest:
```bash
pytest test_project.py
