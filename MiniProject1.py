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



## Global variable setup:


toDoList = []
dueList = []
priorityList = []
completionList = []

ColorReset = '\033[m' # reset to the defaults
ColorBlue = '\033[34m' # Green Text
ColorGreen =  '\033[32m' # Green Text


print("Welcome to your To-Do List App! :)")

#Function Setup

#Create clamp for task priority
def clamp(n, min, max):
    if n < min :
        return str(min)
    if n > max:
        return str(max)
    else:
        return str(n)
    
##Function to display To-Do list

def listDisplay():   
    if bool(toDoList) != False:
        for i, element in enumerate(toDoList):
            print("name:", element, " --- ", "due:", dueList[i], " --- ", "priority:", priorityList[i], " --- ", "status:", completionList[i])
    else:
        print("There's Nothing here! Your To-Do list is empty :)")
    print("\n")

##For resetting local variables in add task features
def resetTaskVariables():
    taskTitle=""
    taskDue=""
    taskPriority=""

##For changing text colour upon task completion
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
    
#Add task function
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
    
#Display To-Do list function
def viewTasks():
    print("\nOk let's pull up your To-Do List:\n")
    listDisplay()
    print("\n")

#Function to mark task as complete -- within which we call the changeColor function
def markAsComplete(task):
    global completionList
    #What's the name of the Task you want to change to complete?
    x = 0
    foundItem = False
    
    while x < len(toDoList):
        if task in toDoList[x].lower():
            taskIndex = x
            foundItem = True
            break
        else:
            x +=1
    
    if foundItem != False:
        changeColor(taskIndex)
        completionList[taskIndex] = completionList[taskIndex].replace("Incomplete", "Complete")

        print(f"\nYou've succesfully changed task {toDoList[x]} from Incomplete to Complete!\n")
        listDisplay()
        print("\n")
    else:
        print(f"\nCouldn't find a task named {task}. Make sure you enter a real task name!\n")
            

#Function for deleting a task
def delTask(task):
    global toDoList
    global dueList
    global priorityList
    global completionList

    x = 0
    taskLower = task.lower()
    
    foundItem = False
    
    while x < len(toDoList):
        if taskLower in toDoList[x].lower():
            taskIndex = x
            foundItem = True
            break
        else:
            x +=1

    if foundItem != False:
        toDoList.pop(taskIndex)
        dueList.pop(taskIndex)
        priorityList.pop(taskIndex)
        completionList.pop(taskIndex)

        print(f"\nOk, the task '{task}' was succesfully removed from the list!")
        print("Your To-Do list now looks like this:\n")
        listDisplay()
        print("\n")
    else:
        print(f"\nTask '{task}' not found on To-Do list. Are you sure you entered the right name?\n")

##Main program while loop
while True:
    print("Please make a selection from the following menu: (Feel free to use the item number or name, or both!)")
    print(" 1. Add a task\n 2. View tasks\n 3. Mark a task as complete\n 4. Delete a task\n 5. Quit")

    try:
        userSelection = input("Which list item would you like to select?\n").strip()
        #check to make sure only one digit in selection

    except:
        print("\nPlease make sure you enter a valid selection\n")

    else:
                #check to make sure is all either digit or alpha else throw print statement
        if userSelection.lower() == "add a task" or userSelection.lower() == "1" or "1" in userSelection:

            print("Ok, lets add a new task!\n")
            
            #task creation variable input
            #check task title for errors    
            try:
                taskTitle = input("Please enter a title for your new task:\n").strip() or "Incomplete"
            except ValueError:
                print("Make sure you put in an actual answer!")
            except OverflowError:
                print("Make sure you don't overwhelm the system!")
                
            #check task due for errors
            try:
                taskDue = input(f"Please enter a due date for {taskTitle}. (If no due date desired please leave empty)\n").strip() or False
            except OverflowError:
                print("Make sure you don't overwhelm the system!")
            

            #check task priority for errors
            try:
                taskPriority = int(input(f"Please enter a priority number for the task between 0 and 5 (0 being lowest priority in 5 being highest.) \nIf no priority number desired please leave empty.\n").strip() or 0)
            except ZeroDivisionError:
                print("Don't divide by zero!")
            except ValueError:
                print("Make sure you enter a valid Number between 0 and 5 - or leave blank!")
            else:
                #clamping the priority integer between 0 and 5
                if bool(taskPriority) != False:
                    taskPriority = clamp(taskPriority,0,5)
                else:
                    taskPriority = taskPriority

                #check for empty responses, tailor print statement and function call to each case:
            if bool(taskTitle) == True and bool(taskDue) == False and bool(taskPriority) == False:
                print(f"Great, you want to add a task called {taskTitle}.")
                print("Lets add that to your to do list!\n")
                addTask(taskTitle)
                resetTaskVariables()
                print("Task added succesfully! Variables cleared for next time!\n")
                
            elif bool(taskTitle) == True and bool(taskDue) == True and bool(taskPriority) == False:
                print(f"Great. You want to add a task called {taskTitle} with a due date of {taskDue}")
                print("Lets add that to your to do list!\n")
                addTask(taskTitle, taskDue)
                resetTaskVariables()

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
                #catch-all
                print("\nAn error occurred!")
                #reset local variables for task creation
                resetTaskVariables()
           

        elif userSelection.lower() == "view tasks" or userSelection.lower() == "2" or "2" in userSelection:
            viewTasks()

        elif userSelection.lower() == "mark a task as complete" or userSelection.lower() == "3" or "3" in userSelection:

            if bool(toDoList) != False:
                print("Great job on completing one of your tasks! Lets scratch it off the list")
                try:
                    finishedTaskLower = input("Which task did you complete?\n").lower()
                except:
                    print("Make sure you enter a real task name!")
                else:
                    if bool(finishedTaskLower) != False:
                        markAsComplete(finishedTaskLower)
                    else:
                        print("\nMake sure you enter a valid task name! Try again:\n")
            else:
                print("\nYou can't mark a task as complete when you don't have any tasks on your list! Try adding something first :)\n")

        elif userSelection.lower() == "delete a task" or userSelection.lower() == "4" or "4" in userSelection:
            if bool(toDoList) != False:
                print("\nOk, lets remove a task.")
                try:
                    removeTaskLower = input("Which task would you like to remove?\n").strip()
                except:
                    print("Make sure you enter a real task name!")
                else:
                    if bool(removeTaskLower) != False:
                        delTask(removeTaskLower)
                    else:
                        print("\nMake sure you enter a valid task name! Try again:\n")
            else:
                print("\nYou can't remove a task from an empty list! Try adding something first :)\n")
                
            #check input for character values
            

        elif userSelection.lower() == "quit" or userSelection.lower() == "5" or "5" in userSelection:
            print("Thanks for stopping by, see you soon!")
            break
            #quit program
        
        else:
            print("\nPlease make sure you select a valid list item!\n")
            #default list error display
        