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



## Global variable and text color setup:


toDoList = []
dueList = []
priorityList = []
completionList = []
# ColorList = []

ColorReset = '\033[m' # reset to the defaults
ColorBlue = '\033[34m' # Green Text
ColorGreen =  '\033[32m' # Green Text
# print (TGREEN + "Das ist es!" , ENDC)
# print (TBLUE + "Das ist es!" , ENDC)

print("Welcome to your To-Do List App!")

def listDisplay():
    
    if bool(toDoList) != False:
        for i, element in enumerate(toDoList):
            print("name:", element, " --- ", "due:", dueList[i], " --- ", "priority:", priorityList[i], " --- ", "status:", completionList[i])
    else:
        print("There's Nothing here! Your To-Do list is empty :)")
    print("\n")

def resetTaskVariables():
    taskTitle=""
    taskDue=""
    taskPriority=""

def changeColor(index):
    global toDoList
    global dueList
    global priorityList
    global completionList

    toDoList[index] = toDoList[index].replace(ColorBlue, ColorGreen)
    dueList[index] = dueList[index].replace(ColorBlue, ColorGreen)
    priorityList[index] = priorityList[index].replace(ColorBlue, ColorGreen)
    completionList[index] = completionList[index].replace(ColorBlue, ColorGreen)
    print("Text Color Changed...")
    

def addTask(task, dueDate="n/a", priority="n/a"):
    global toDoList
    global dueList
    global priorityList
    global completionList

    toDoList.append(ColorBlue + task + ColorReset)
    dueList.append(ColorBlue + dueDate + ColorReset)
    priorityList.append(ColorBlue + priority + ColorReset)
    completionList.append(ColorBlue + "Incomplete" + ColorReset)

    listDisplay()
    
def viewTasks():
    print("\nOk let's pull up your To-Do List:\n")
    listDisplay()
    print("\n")


def markAsComplete(task):
    global completionList
    #What's the name of the Task you want to change to complete?
    x = 0
    
    while x < len(toDoList):
        if task in toDoList[x].lower():
            taskIndex = x
            break
        else:
            print("Couldn't find, added 1 to x")
            x +=1

    changeColor(taskIndex)
    completionList[taskIndex] = completionList[taskIndex].replace("Incomplete", "Complete")

    print(f"\nYou've succesfully changed task {toDoList[x]} from Incomplete to Complete!\n")
    listDisplay()
    print("\n")

def delTask(task):
    global toDoList
    global dueList
    global priorityList
    global completionList

    x = 0
    taskLower = task.lower()
    
    while x < len(toDoList):
        if taskLower in toDoList[x].lower():
            taskIndex = x
            break
        else:
            print("Couldn't find, added 1 to x")
            x +=1
    else:
        print(f"Task '{task}' not found on To-Do list. Are you sure you entered the right name?")

    toDoList.pop(taskIndex)
    dueList.pop(taskIndex)
    priorityList.pop(taskIndex)
    completionList.pop(taskIndex)

    print(f"\nOk, the task '{task}' was succesfully removed from the list!")
    print("Your To-Do list now looks like this:\n")
    listDisplay()
    print("\n")
    
    


while True:
    print("Please make a selection from the following menu: (Feel free to use the item number or name, or both!)")
    print(" 1. Add a task\n 2. View tasks\n 3. Mark a task as complete\n 4. Delete a task\n 5. Quit")

    try:
        userSelection = input("Which item would you like to select?\n").strip()
        #check to make sure only one digit in selection

    except ValueError:
        print("\nPlease make sure you enter a valid selection\n")

    else:
                #check to make sure is all either digit or alpha else throw print statement
        if userSelection.lower() == "add a task" or userSelection.lower() == "1" or "1" in userSelection:

            print("Ok, lets add a new task!\n")
            
            #task creation variable input
            taskTitle = input("Please enter a title for your new task:\n").strip()
                #check task title for errors
            taskDue = input(f"Please enter a due date for {taskTitle}. (If no due date desired please leave empty)\n").strip() or False
                #check task due for errors
            taskPriority = input(f"Please enter a priority number for the task between 1 and 5 (1 being lowest priority in 5 being highest.) \nIf no priority number desired please leave empty.\n").strip() or False
                #check task priority for errors

                #check for empty responses, tailor print statement and function call to each case:
            if bool(taskTitle) == True and bool(taskDue) == False and bool(taskPriority) == False:
                print(f"Great. You want to add a task called {taskTitle}.")
                print("Lets add that to your to do list!\n")
                addTask(taskTitle)
                resetTaskVariables()
                print("Task added succesfully! Variables cleared for next time!\n")
                
            elif bool(taskTitle) == True and bool(taskDue) == True and bool(taskPriority) == False:
                print(f"Great. You want to add a task called {taskTitle} with a due date of {taskDue}")
                print("Lets add that to your to do list!\n")
                addTask(taskTitle, taskDue)
                resetTaskVariables()
                print("Task added succesfully! Variables cleared for next time!\n")

            elif bool(taskTitle) == True and bool(taskDue) == True and bool(taskPriority) == True:
                print(f"Great. You want to add a task called {taskTitle}, with a due date of {taskDue} and a priority number of {taskPriority}.")
                print("Lets add that to your to do list!\n")
                addTask(taskTitle, taskDue, taskPriority)
                resetTaskVariables()
                print("Task added succesfully! Variables cleared for next time!\n")
                
            elif bool(taskTitle) == True and bool(taskDue) == False and bool(taskPriority) == True:
                print(f"Great. You want to add a task called {taskTitle} with a priority of {taskPriority}")
                print("Lets add that to your to do list!\n")
                addTask(taskTitle, "n/a", taskPriority)
                resetTaskVariables()
                print("Task added succesfully! Variables cleared for next time!\n")

            else:
                print("\nAn error occurred!")
              #  print(f"task title = {taskTitle}, task due = {taskDue}, task priority = {taskPriority}")
                resetTaskVariables()
                print("Task variables cleared for next time!\n")
                
        
            
            #check task title for correct values
            #check task due for correct values
            #check task priority for correct values, use ceiling and floor to cut off the numbers. Make sure is int.
            #check to see which fields are empty and tailor function call for each case so default values are used when desired.
            #color orange for 'in progress' and green for 'completed'
            #function call

            #reset task creation variables
           

        elif userSelection.lower() == "view tasks" or userSelection.lower() == "2" or "2" in userSelection:
            print("Ok, lets take a look at your to do list!")
            #remember color coding
            #function call

        elif userSelection.lower() == "mark a task as complete" or userSelection.lower() == "3" or "3" in userSelection:
            print("Great job on completing one of your tasks! Lets scratch it off the list")
            finishedTaskLower = input("Which task did you complete?\n").lower()
            markAsComplete(finishedTaskLower)
            #taking input taskname as lowercase to reduce user error - remember to check for task name lowercase
            #check finished task name for correct values using try except
            #change color to green
            #function call

        elif userSelection.lower() == "delete a task" or userSelection.lower() == "4" or "4" in userSelection:
            print("Ok, lets remove a task.")
            removeTaskLower = input("Which task would you like to remove?\n")
            delTask(removeTaskLower)
            
            #check input for character values
            

        elif userSelection.lower() == "quit" or userSelection.lower() == "5" or "5" in userSelection:
            print("Thanks for stopping by, see you soon!")
            break
            #quit program somehow
        
        else:
            print("Please make sure you select a valid list item!")
        