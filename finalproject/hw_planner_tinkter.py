from datetime import date, datetime
import tkinter as tk
from tkinter import simpledialog, messagebox, Button, Frame, ttk

# Function will read the file that has been given in main function.
def read_file(file):
    '''Reading the contents of the text file and create it 
    into a dictionary.
    Parameters:
        file: the name of the text file.
    Return: a dictionary
    '''
    dictionary = {}

    # Opening the file with rt.
    with open(file, "rt") as filename:

        # Going through all the rows in the file.
        for row in filename:
            
            # Splitting the rows with the ','.
            row_list = [item.strip() for item in row.split(",")]

            # Getting the first item in the key
            key = row_list[0]

            # If the key is not in dictionary, add t to the empty list.
            if key not in dictionary:
                dictionary[key] = []
            
            # Append the list to the dictionary.
            dictionary[key].append(row_list)

    return dictionary

# This Function will add the task to the txt file.
def adding_task(file_name, priority, deadline, name):
    '''Adding an assignment or project to the text file. then
        will be added what number of priority it will be in.
    Parameters:
        file_name: The text file
    Return: Adding the assignment or project to the file
    '''

    # Opens the given file with 'read'.
    with open(file_name, "r") as file:
        # reading the lines in the file.
        tasks = file.readlines()
    
    # Adding the priority, deadline, and name given to the tasks variable.
    tasks.append(f'{priority}, {deadline}, {name}\n')

    # Opening the file again with 'write'.
    with open(file_name, "w") as file:

        # Adding the tasks to the txt file.
        file.writelines(tasks)

    return file

# This function will display all the tasks
def display_all_tasks(file):
    '''' Displaying all of the tasks for the week.
    Parameters:
        file: text file
    Return: Displaying all the assignments and projects in the file
    '''
    # Reading the given file.
    homework_file = read_file(file)

    # Creating a variable that calculates the total number of assignments in the file.
    message_box = f"Total Assignments: {sum(len(assignment) for assignment in homework_file.values())}\n"
    
    # Iterating through all the assignments in the file.
    for assignment in homework_file.values():

        # Iterating through the assignments in the list.
        for assignments in assignment:

            # Adding each assignment to the variable.
            message_box += f"{assignments[2]}: Deadline:{assignments[1]}, Priority:{assignments[0]} \n"

    # Displaying the assignments with tinkter.
    messagebox.showinfo("Assignments", message_box)

# This function will display the assignments for today.
def display_day_tasks(file):
    ''' Displaying the day of the date the user chose. Then 
    it will display all the assignments and projects for 
    that day.
    Parameters:
        file: the text file
    Return: Display the assignments and projects for that specific day.
    '''
    
    # Finding Today's date.
    today_date = str(date.today())
    time = datetime.now()

    # Reading the file that was given.
    homework_file = read_file(file)

    assignments = []

    # Iterating through the tasks in the file.
    for task in homework_file.values():

        # Iterating through the homework in the task.
        for home_work in task:

            # If the home_work has today's date, then it will be added to the dictionary.
            if home_work[1] == today_date:
                assignments.append(home_work)

    message_box = ""

    # Iterating through the homework in the assignments dictionary.
    for work_name in assignments:
        message_box += f"Priority:{work_name[0]}, Name: {work_name[2]}: Deadline: {work_name[1]}\n"

    # If there is assignments with today's date, then it will show.
    if message_box:
        messagebox.showinfo(f"({today_date}, {time.strftime("%I:%M:%S")}) Today's Assignments are", message_box)
    else:
        messagebox.showinfo("Today's Assignments are", "There are not Assignments today!")

# This function will delete a tasks from the txt file.
def mark_complete(file, name):
    '''Find the name in the file and then mark/delete the assignment 
    or project from the file.
    Parameters:
        file: The text file
        name: Name of the assignment or project they want to see
    Return: Deletes the name from the file.
    '''

    # Opening and reading the file that was given.
    with open(file, "r") as file_name:
        lines = file_name.readlines()

    found_assignment = False

    # Opening and writing in the txt file.
    with open(file, "w") as file_name:

        # Iterating through the lines in the file.
        for line in lines:

            # If there is an assignment under the name, then it is deleted.
            if name not in line.strip():
                file_name.write(line)
            else:
                found_assignment = True
    
    # If the assignment was deleted it will state complete.
    if found_assignment == True:
        messagebox.showinfo("Task Complete", "Nice Job!")
    else:
        messagebox.showinfo("Task Not Complete", "There are not assignments under that name.")

# The main function that initiates through everything.
def main():

    # Creating tinkter window.
    main_tk = tk.Tk()

    # The title and size of the tinkter window.
    main_tk.title("Homework Calendar")
    main_tk.geometry("680x680")

    # If user selects add task, then it will initiate add_task function.
    def add_task():
        name = simpledialog.askstring("Input", "Please enter the assignment:")
        priority = simpledialog.askinteger("Input", "Please enter the priority of assignment from 1-5:")
        deadline = simpledialog.askstring("Input", "Please enter the date in format year-month-day (xxxx-xx-xx):")
        adding_task("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", priority, deadline, name)

    # Initiates the display_all_tasks function
    def display_all():
            display_all_tasks("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")

    # Initiates the display_day_tasks function
    def display_tool_today():
            display_day_tasks("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt")

    # Initiates the mark_complete function
    def complete_assignment():
            name_assignment = simpledialog.askstring("Input","Please enter the name of the assignmnet:")
            mark_complete("C:/Users/lover/Documents/CSE 111/finalproject/school_assignments.txt", name_assignment)

    # Adds background color to the buttons while mousing over.
    def enter_add(e):
        add_button["background"] = "pink"
    
    # Adds background color to the buttons without mousing over.
    def leaving_add(e):
        add_button["background"] = "SystemButtonFace"

    # Adds background color to the buttons while mousing over.
    def enter_all_display(e):
        display_all_button["background"] = "pink"

    # Adds background color to the buttons without mousing over.
    def leaving_all_display(e):
        display_all_button["background"] = "SystemButtonFace"

    # Adds background color to the buttons while mousing over.
    def enter_today(e):
        display_today_button["background"] = "pink"

    # Adds background color to the buttons without mousing over.
    def leaving_today(e):
        display_today_button["background"] = "SystemButtonFace"

    # Adds background color to the buttons while mousing over.
    def enter_complete(e):
        complete_button["background"] = "pink"

    # Adds background color to the buttons without mousing over.
    def leaving_complete(e):
        complete_button["background"] = "SystemButtonFace"

    # Creating the frame for the buttons.
    button_frame = Frame(main_tk)
    button_frame.pack(fill=tk.X, ipadx=5, ipady=5)

    # Creating a button for add_tasks function.
    add_button = Button(button_frame, text="Add Task", command=add_task, width=30, height=5, bd=20)
    add_button.grid(row=1, column=0, padx=10, pady=10)
    add_button.bind("<Enter>", enter_add)
    add_button.bind("<Leave>", leaving_add)

    # Creating a button for display_all.
    display_all_button = Button(button_frame, text="Display All", command=display_all, width=30, height=5, bd=20)
    display_all_button.grid(row=2, column=0, padx=10, pady=10)
    display_all_button.bind("<Enter>", enter_all_display)
    display_all_button.bind("<Leave>", leaving_all_display)

    # Creating a button for display_day_tasks.
    display_today_button = Button(button_frame, text="Today Display", command=display_tool_today, width=30, height=5, bd=20)
    display_today_button.grid(row=3, column=0, padx=10, pady=10)
    display_today_button.bind("<Enter>", enter_today)
    display_today_button.bind("<Leave>", leaving_today)

    # Creating a button for complete_assignment.
    complete_button = Button(button_frame, text="Complete Assignment", command=complete_assignment, width=30, height=5, bd=20)
    complete_button.grid(row=4, column=0, padx=10, pady=10)
    complete_button.bind("<Enter>", enter_complete)
    complete_button.bind("<Leave>", leaving_complete)

    # Centering the buttons in the window.
    button_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Start the tinkter loop.
    main_tk.mainloop()

if __name__ == "__main__":
    main()
