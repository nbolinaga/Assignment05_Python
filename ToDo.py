# ------------------------------------------------- #
# Title: Working with Dictionaries
# Dev:   RRoot, Nicolas Bolinaga
# Date Created:  July 16, 2012
#  > RRoot, 11/02/2016, Created starting template
#  > Nicolas Bolinaga, 8/12/2019, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# ------------------------------------------------- #

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------

# VARIABLES
strData = ""
lstTable = []
dic = {}

# FUNCTIONS


def read_file():
    # Opens the .txt file as a readable file
    objFileName = open("C:\_PythonClass\Assignment05\ToDo.txt", "r+")
    # For each line in the file strip it down
    for line in objFileName:
        # Separates the key and the value by a comma (,)
        key, value = line.strip().split(',')
        # Saves the key and the value as a variable called dic{}
        dic = {key, value}
        # Appends dic{} to the list (lstTable)
        lstTable.append(dic)
    # Closes the file wiping it clean
    objFileName.close()


def add_item():
    # Asks user to input a task and saves it as new_item
    print(f'Input the task below to add it to the list ')
    new_item = input(f'>>>>')
    # Asks user to input a priority and saves it as new_priority
    print(f'Input the priority level of the task below')
    new_priority = input(f'>>>>')
    print()
    # Joins both into a dictionary called new_dic as key, value pair
    new_dic = {new_item, new_priority}
    # Asks the user to verify their input is correct
    print(f'You typed {new_dic}\nAre you sure you want to add it to your list?\n\t1) Yes\n\t2) No')
    user_answer = input(f">>>>")
    # Checks if their response is "yes"
    # If so:
    if user_answer == '1':
        # Appends new dictionary to list and display success message with new updated list
        lstTable.append(new_dic)
        print(f'\n{new_dic} added to your list!\n')
        print(f'You have {len(lstTable)} item/s in your list.\n')
        print(*lstTable, sep="\n")
    # Anything else displays error message and reruns the function
    else:
        print(f'\nNo items added to your list\nTry Again...\n')
        add_item()


def remove_item():
    # Gives each item within the list a index number
    for number, task in enumerate(lstTable):
        print(number, task)
    # Asks the user to input one of the numbers showed above
    print("\nInput below the number of the task you would like to erase")
    user_input = input(">>>>")
    # Tries if the input is in fact a number
    try:
        user_input = int(user_input)
        # If it is in fact a number it then checks if the number is within range.
        if user_input < len(lstTable) and user_input >= 0:
            # If number is within range pop (remove) the chosen item from list
            removed_item = lstTable.pop(user_input)
            # Shows the removed item plus the updated list
            print(f'\n{removed_item} removed from your list!\n')
            print(f'You now have {len(lstTable)} item/s in your list.\n')
            print(*lstTable, sep="\n")
        else:
            print(f"\n{user_input} is not a valid number.\n Try again...\n")
            remove_item()
    # If its not a number print error message and rerun function
    except ValueError:
        print(f"\n{user_input} is not a valid number.\n Try again...\n")
        remove_item()


def save_items():
    # Opens the .txt file
    objFileName = open("C:\_PythonClass\Assignment05\ToDo.txt", "r+")
    # Converts dictionaries into strings separating them by a comma
    # Converts the list into a string separated by a "\n" (new line)
    # Saves it as a variable called "fullStr"
    fullStr = '\n'.join([str(','.join(task)) for task in lstTable])
    # Writes the variable into the text file
    objFileName.write(f"{fullStr}")
    # Prints success message and closes the file
    print(f"{fullStr}\n\nList saved to text file")
    objFileName.close()


# Step 1 - Load data from a file
read_file()

# Step 2 - Display a menu of choices to the user
while (True):
    print("____________________________________________________________________\n")
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if strChoice.strip() == '1':
        print(f'You have {len(lstTable)} item/s in your list.\n')
        print(*lstTable, sep="\n")
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        add_item()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif strChoice == '3':
        remove_item()
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif strChoice == '4':
        save_items()
        continue
    elif strChoice == '5':
        break  # and Exit the program

