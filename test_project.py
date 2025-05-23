import pytest
from project import get_tasks, save_tasks, add_task, remove_task

def test_get_tasks():
    with open("tasks.txt", "w") as file:
        file.write("Test Task 1\nTest Task 2\n")
    tasks = get_tasks()
    assert tasks == ["Test Task 1", "Test Task 2"]

def test_save_tasks():
    tasks = ["Task 1", "Task 2"]
    save_tasks(tasks)
    with open("tasks.txt", "r") as file:
        saved_tasks = file.read().splitlines()
    assert saved_tasks == tasks

def test_add_task():
    task = "New Task"
    save_tasks([])  # Clear the current tasks
    add_task(task)
    tasks = get_tasks()
    assert task in tasks

def test_remove_task():
    tasks = ["Task 1", "Task 2"]
    save_tasks(tasks)
    remove_task(0)  # Remove the first task
    tasks = get_tasks()
    assert "Task 1" not in tasks

if __name__ == "__main__":
    pytest.main()
 