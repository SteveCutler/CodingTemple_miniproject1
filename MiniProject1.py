# Introduction

# In this project, you will apply your Python programming skills to 
# create a functional To-Do List Application from scratch. The objective 
# of this project is to reinforce your understanding of Python syntax, 
# data types, control structures, functions, and error handling while 
# building a practical and interactive application.


# Project Requirements

#     User Interface (UI):

#         Create a command-line interface (CLI) for the To-Do List Application.

#         Display a welcoming message and a menu with the following options:

#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit

#     To-Do List Features:
#         Implement the following features for the To-Do List:
#             Adding a task with a title (by default “Incomplete”).
#             Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
#             Marking a task as complete.
#             Deleting a task.
#             Quitting the application.

#     User Interaction:
#         Allow users to interact with the application by selecting menu options using input().
#         Implement input validation to handle unexpected user input gracefully.

#     Error Handling:
#         Implement error handling using try, except, else, and finally blocks to handle potential issues.

#     Code Organization:
#         Organize your code into functions to promote modularity and readability.
#         Use meaningful function names with appropriate comments and docstrings for clarity.

#     Testing and Debugging:
#         Thoroughly test your application to identify and fix any bugs.
#         Consider edge cases, such as empty task lists or incorrect user input.

#     Documentation:
#         Include a README file that explains how to run the application 
#         and provides a brief overview of its features.

#     Optional Features (Bonus):
#         If you feel adventurous, you can add extra features like task 
#         priorities, due dates, or color-coding tasks based on their status.

#     GitHub Repository:
#         Create a GitHub repository for your project.
#         Commit your code to the repository regularly.
#         Include a link to your GitHub repository in your project documentation.

# Submission

#     Submit your project, including all source code files and the README, 
#     to your instructor or designated platform.

# Project Tips

#     Start by designing a simple user interface and plan the program's structure.
#     Test your code frequently as you build each feature to ensure everything works as expected.
#     Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!


#####################

#Create a CLI ???

#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit

#     To-Do List Features:
#         Implement the following features for the To-Do List:
#             Adding a task with a title (by default “Incomplete”).
#             Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
#             Marking a task as complete.
#             Deleting a task.
#             Quitting the application.

#     Optional Features (Bonus):
#         If you feel adventurous, you can add extra features like task 
#         priorities, due dates, or color-coding tasks based on their status.

print("Welcome to the To-Do List App!")
print("Please make a selection from the following menu: (Feel free to use the item number or name, but not both!)")
print(" 1. Add a task\n 2. View tasks\n 3. Mark a task as complete\n 4. Delete a task\n 5. Quit")

def addTask(task, dueDate="n/a", priority="0"):
    #colorCoding
    pass

def viewTasks():
    #colorCoding
    pass

def markAsComplete(task):
    #colorCoding
    pass

def delTask(task):
    pass

def quit():
    pass

try:
    userSelection = input("Which item would you like to select?\n")
except ValueError:
    print("Please make sure you enter a valid selection")
else:
    if userSelection.lower() == "add a task" or userSelection.lower() == "1":
        print("you selected task 1")
    elif userSelection.lower() == "view tasks" or userSelection.lower() == "2":
        print("you selected task 2")
    elif userSelection.lower() == "mark a task as complete" or userSelection.lower() == "3":
        print("you selected task 3")
    elif userSelection.lower() == "delete a task" or userSelection.lower() == "4":
        print("you selected task 4")
    elif userSelection.lower() == "quit" or userSelection.lower() == "5":
        print("you selected task 5")
    else:
        print("Please make sure you select a valid list item!")
    