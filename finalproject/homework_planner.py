from datetime import date
import tkinter as tk
from tkinter import simpledialog, messagebox, Button

def read_file(file):
    '''Reading the contents of the text file and create it 
    into a dictionary.
    Parameters:
        file: the name of the text file.
    Return: a dictionary
    '''
    dictionary = {}

    with open(file, "rt") as filename:

        for row in filename:
        
            row_list = [item.strip() for item in row.split(",")]

            key = row_list[0]

            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(row_list)

    return dictionary

def adding_task(file_name, priority, deadline, name):
    '''Adding an assignment or project to the text file. then
        will be added what number of priority it will be in.
    Parameters:
        file_name: The text file
    Return: Adding the assignment or project to the file
    '''

    with open(file_name, 'r') as file:
        tasks = file.readlines()
    
    tasks.append(f'{priority}, {deadline}, {name}\n')

    with open(file_name, 'w') as file:
        file.writelines(tasks)

    return file

def display_all_tasks(file):
    '''' Displaying all of the tasks for the week.
    Parameters:
        file: text file
    Return: Displaying all the assignments and projects in the file
    '''
    homework_file = read_file(file)

    message_box = f'Total Assignments: {sum(len(assignment) for assignment in homework_file.values())}\n'
    
    for assignment in homework_file.values():
        for assignments in assignment:
            message_box += f"{assignments[2]}: Deadline:{assignments[1]}, Priority:{assignments[0]} \n"

def display_day_tasks(file):
    ''' Displaying the day of the date the user chose. Then 
    it will display all the assignments and projects for 
    that day.
    Parameters:
        file: the text file
    Return: Display the assignments and projects for that specific day.
    '''
    today_date = str(date.today())

    homework_file = read_file(file)
    assignments = []
    for task in homework_file.values():
        for home_work in task:
            if home_work[1] == today_date:
                assignments.append(task)

    message_box = ""
    for work_name in assignments:
        print(work_name)
        message_box += f"Priority:{work_name[0]}, Deadline:{work_name[1]}, Name:{work_name[2]}\n"

def mark_complete(file, name):
    '''Find the name in the file and then mark/delete the assignment 
    or project from the file.
    Parameters:
        file: The text file
        name: Name of the assignment or project they want to see
    Return: Deletes the name from the file.
    '''
    with open(file, 'r') as file_name:
        lines = file_name.readlines()

    found_assignment = False
    with open(file, 'w') as file_name:
        for line in lines:
            if name not in line.strip():
                file_name.write(line)
            else:
                found_assignment = True
    if found_assignment == True:
        print("Task Complete", "It is completed!")
    else:
        print("Task Not Complete", "There are not assignments under that name.")

def main():

    
    choice = 1

    while choice != 0:
        print("Main menu")
        print("1. Adding an assignment")
        print("2. Displaying all tasks")
        print("3. Finding a task for today")
        print("4. Completing an assignment")
        print("0. End")
        choice = int(input("Please choose a number:"))
        if choice == 1:
            name = input("Please enter the assignment:")
            priority = int(input("Please enter the priority of assignment from 1-5:"))
            deadline = str(input("Please enter the date in format year-month-day (xxxx-xx-xx):"))
            adding_task("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", priority, deadline, name)
        elif choice == 2:
            display_all_tasks("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")
        elif choice == 3:
            display_day_tasks("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")
        elif choice == 4:
            name_assignment = input("Please enter the name of the assignmnet:")
            mark_complete("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", name_assignment)

    


if __name__ == "__main__":
    main()
