Documentation for To-Do app:

On launching the application you will be prompted with a menu of options:

 1. Add a task
 2. View tasks
 3. Mark a task as complete
 4. Delete a task
 5. Quit

It's pretty self explanatory but I'll go into detail about each of the features and how they function:

        1. Add a Task:
    Your To-Do list starts off empty, so naturally options 3 and 4 won't do anything until a task is added.
    On selecting the Add a Task option you will be prompted with providing a task name. You can enter whatever you want, and if you leave it blank it will default to "Incomplete" as per the instructions.
    
    You will then be prompted for a due date. If left empty it will default to "n/a", but you can input a due date in whatever format you wish, e.g. "Dec 12", "Tomorrow", "12pm" etc.

    One final prompt for adding a task will then appear asking you to enter a priority number between 0 and 5. If a number is entered outside this range the clamp() function will clamp it between this range. If a float or string are entered it will default to "0". It will also default to "0" if left blank.

    The task list will then be displayed and its default status will be "Incomplete". Incomplete items will appear blue in the list.

###

        2.View tasks
    This choice calls the function to display the To-Do list.

###

        3.Mark a task as Complete
    This option prompts you for the task name. If nothing is entered or a task that doesn't exist it will print a message and return you to the menu.
    If the user enters a correct task name, the corresponding task status will be changed from "Incomplete" to "Complete" and the colour of the task in the To-Do list will change from Blue to Green and it will display it like this from now on.

###

        4.Delete a task
    This option prompts the user for a task name once again. Similarly to the "Mark a task as complete" option, if the prompt is left empty or a task that doesn't exist is entered, the program will print a prompt telling you to make sure you enter a real task.
    If a task is correctly entered, the task will be removed from the ToDo list and the new list will be displayed.

###

        5.Quit
    This quits the 'while' loop that effectively keeps the program running. The program is exited and the list data will not be retained.
