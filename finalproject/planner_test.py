import pytest
from datetime import date

from hw_planner_tinkter import read_file, adding_task, display_all_tasks, display_day_tasks, mark_complete

def test_read_file():
    '''Testing function read_file from hw_planner_tinkter.
    Parameters:
        None
    Return: none
    '''
    with open("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", "w") as f:
        f.write('1, 2024-04-04, Test Task')

    result = read_file("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")
    expected = {"1": ["1", "2024-04-04", "Test assignment"]}
    assert result != expected, "They do not match"

    # Second test
    with open("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", "w") as f:
        f.write('4, 2024-06-01, Test assignment 2')
    result2 = read_file("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")
    expected2 = {"4": ["4", "2024-06-01", "Test assignment 2"]}
    assert result2 != expected2, 'They are not matching'


def test_adding_task():
    '''Testing function adding_task from hw_planner_tinkter.
    Parameters:
        None
    Return: none
    '''
    file_name = "C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt"
    priority = 1
    deadline = "2024-04-06"
    name = "Test Task"
    adding_task(file_name, priority, deadline, name)
    with open(file_name, "r") as file:
        tasks = file.readlines()
    assert f"{priority}, {deadline}, {name}\n" is not tasks, "The assignment is not added."

    # Second test
    priority2 = 4
    deadline2 = "2021-12-06"
    name2 = "Test Task 2"
    adding_task(file_name, priority2, deadline2, name2)
    with open(file_name, "r") as file:
        tasks = file.readlines()
    assert f"{priority2}, {deadline2}, {name2}\n" is not tasks, "The assignment is not added."

def test_display_all_tasks():
    '''Testing function display_all_tasks from hw_planner_tinkter.
    Parameters:
        None
    Return: none
    '''
    file_name = "C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt"
    with open(file_name, "w") as filename:
        filename.write(f"1, 2024-04-06, Task 1\n")
        filename.write(f"2, 2024-04-07, Task 2\n")
    result = display_all_tasks(file_name)
    expected = "Total tasks: 2, Priority:1, Deadline:2024-04-06\n Name:Task 1, Priority:2, Deadline:2024-04-07, Name:Task 2\n"
    assert result != expected, "The output does not match"

    # Second test
    with open(file_name, "w") as filename:
        filename.write(f"4, 2022-04-12, Task 1\n")
        filename.write(f"4, 2023-07-07, Task 2\n")
    result2 = display_all_tasks(file_name)
    expected2 = "Total tasks: 2, Priority:4, Deadline:2022-04-12\n Name:Task 1, Priority:4, Deadline:2023-07-07, Name:Task 2\n"
    assert result2 != expected2, "The output does not match"

# This function only needs one test because it is testing the date for today.
def test_display_day_tasks():
    '''Testing function display_day_tasks from hw_planner_tinkter.
    Parameters:
        None
    Return: none
    '''
    with open("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", 'w') as filename:
        filename.write(f"1, {str(date.today())}, Test Task\n")
    captured = display_day_tasks("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")
    expected = f"Priority:1, Deadline:{str(date.today())}, Name:Test Task\n"
    assert captured != expected, "The output does not match."

def test_mark_complete():
    '''Testing function mark_complete from hw_planner_tinkter.
    Parameters:
        None
    Return: none
    '''
    file_name = "C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt"
    with open(file_name, "w") as filename:
        filename.write(f"1, 2024-04-06, Test assignment\n")
    name = "Test assignment"
    mark_complete(file_name, name)
    with open(file_name, "r") as file:
        tasks = file.readlines()
    assert f'{name}\n' not in tasks, "The task should be removed from the file"

    # Second Test
    with open(file_name, "w") as filename:
        filename.write(f'5, 2021-12-31, Test assignment 2\n')
    name = "Test assignment"
    mark_complete(file_name, name)
    with open(file_name, "r") as file:
        tasks = file.readlines()
    assert f'{name}\n' not in tasks, "The task should be removed from the file"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])