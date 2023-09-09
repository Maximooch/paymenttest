# Simple To-Do List in Python

# Empty list to store to-do items
todo_list = []

# Function to add item to the list
def add_item(item):
    todo_list.append(item)

# Function to remove item from the list
def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)

# Function to view the list
def view_list():
    for item in todo_list:
        print(item)

# Test the functions
add_item("Buy groceries")
add_item("Call mom")
view_list()
remove_item("Buy groceries")
view_list()
