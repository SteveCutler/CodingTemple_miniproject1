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
    #check to make sure is all either digit or alpha else throw print statement
    if userSelection.lower() == "add a task" or userSelection.lower() == "1":

        print("Ok, lets add a new task!")

        taskTitle = input("Please enter a title for your new task:\n")
        taskDue = input(f"Please enter a due date for {taskTitle}. (If no due date desired please leave empty)\n")
        taskPriority = input(f"Please enter a priority number for the task between 1 and 5 (1 being lowest priority in 5 being highest.) If no priority number desired please leave empty.\n")
        #check for empty responses, tailor print statement to each case:
       
        print(f"Great. You want to add a task called {taskTitle}, with a due date of {taskDue} and a priority number of {taskPriority}.")
        print("Lets add that to your to do list!")
        #check task title for correct values
        #check task due for correct values
        #check task priority for correct values, use ceiling and floor to cut off the numbers. Make sure is int.
        #check to see which fields are empty and tailor function call for each case so default values are used when desired.
        #color orange for 'in progress' and green for 'completed'
        #function call

    elif userSelection.lower() == "view tasks" or userSelection.lower() == "2":
        print("Ok, lets take a look at your to do list!")
        #remember color coding
        #function call

    elif userSelection.lower() == "mark a task as complete" or userSelection.lower() == "3":
        print("Great job on completing one of your tasks! Lets scratch it off the list")
        finishedTaskLower = input("Which task did you complete?\n").lower()
        #taking input taskname as lowercase to reduce user error - remember to check for task name lowercase
        #check finished task name for correct values using try except
        #change color to green
        #function call
    elif userSelection.lower() == "delete a task" or userSelection.lower() == "4":
        print("Ok, lets remove a task.")
        removeTask = input("Which task would you like to remove?").lower()
        #converted to lowercase to reduce user error, remember to check for lowercase task on list
        #check input for character values
        #function call
    elif userSelection.lower() == "quit" or userSelection.lower() == "5":
        print("Thanks for stopping by, see you soon!")
        #quit program somehow
    else:
        print("Please make sure you select a valid list item!")
    