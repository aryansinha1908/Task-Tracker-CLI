import json
import os

def create():
    data = {}
    create_name = input("Enter the name of the list to create: ")
    create_name = str(create_name)
    create_name = create_name+".json"
    with open(create_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"To-do list: {create_name} was created successfully.")

def delete():
    delete_name = input("Which list to delete: ") 
    file_path = f"D:\Downloads\Projects\{delete_name}.json"
    try:
        os.remove(file_path)
        print("File deleted successfully")
    except FileNotFoundError:
        print(f"File {delete_name} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_task():
    add_file_name = input("Which list to add the task: ")
    try:
        with open(f"{add_file_name}.json", 'r+') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"List {add_file_name} does not exist")
        return
    add_name = input("What you want to do: ")
    add_date = input("What\'s the deadline: ")
    task_num = len(data)+1
    updates = {task_num: {"Name": add_name,"Due Date": add_date,"Status": "Not done"}}
    data.update(updates)
    with open(f"{add_file_name}.json", 'r+') as file:
        json.dump(data, file, indent=4)
def read_list():
    read_list = input("Which file to view: ")
    with open(f"{read_list}.json", 'r') as file:
        data = json.load(file)
        print(data)

while True:
    command = input("""
    Welcome to Task Tracker, this is a command line interface application to track your to-do lists;
    Command List:- 
    1.) Create a new To-do list
    2.) Manage your tasks im an existing list
    3.) Manage your lists
    4.) Quit the program
    Type the command number in the terminal: 
    """)
    if command == "1":
        create()
    elif command == "2":
        command_2 = input("""
        Task management Commands:-
        1.) Add a new task
        2.) Delete a task
        3.) Update a task
        """)
