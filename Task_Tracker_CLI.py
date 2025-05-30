import json
import os
from datetime import datetime

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
    updates = {task_num: {"Name": add_name,"Due Date": add_date,"Status": "Not done", "Last Update": datetime.now().strftime("%d/%m/20%y")}}
    data.update(updates)
    with open(f"{add_file_name}.json", 'r+') as file:
        json.dump(data, file, indent=4)
    print("Task added successfully")

def delete_task():
    delete_file_name = input("Which list to delete the task from: ")
    try:
        with open(f"{delete_file_name}.json", 'r+') as file:
            data = json.load(file)
            for x in data:
                print(x)
                for y in data[x]:
                    print(y,":",data[x][y])
    except FileNotFoundError:
        print(f"List {delete_file_name} does not exist")
        return
    if data == {}:
        print("The list is empty.")
        return
    delete_task_id = input("Enter the task id to be deleted: ")
    del data[delete_task_id]
    open(f"{delete_file_name}.json", 'w').close()
    with open(f"{delete_file_name}.json", 'r+') as file:
        json.dump(data, file, indent=4)

def update_task():
    update_file_name = input("Which list to update the task from: ")
    try:
        with open(f"{update_file_name}.json", 'r+') as file:
            data = json.load(file)
            for x in data:
                print(x)
                for y in data[x]:
                    print(y,":",data[x][y])
    except FileNotFoundError:
        print(f"List {update_file_name} does not exist")
        return
    update_task_id = input("Enter the task id to be updated: ")
    update_task_property = input("Which property to update: ")
    new_value = input(f"Enter new {update_task_property}: ")
    if update_task_id in data:
        if update_task_property in data[update_task_id]:
            data[update_task_id][update_task_property] = new_value
            data[update_task_id]["Last Update"] = datetime.now().strftime("%d/%m/20%y")
            print(f"Updated {update_task_property} of task {update_task_id} to {new_value}.")
        else:
            print(f"Property {update_task_property} does not exist.")
    else:
        print(f"Task {update_task_id} does not exist.")

    with open(f"{update_file_name}.json", 'w') as file:
        json.dump(data, file, indent=4)


def read_list():
    read_list = input("Which file to view: ")
    with open(f"{read_list}.json", 'r') as file:
        data = json.load(file)
        for x in data:
            print(x)
            for y in data[x]:
                print(y,":",data[x][y])

while True:
    command = input("""
    Welcome to Task Tracker, this is a command line interface application to track your to-do lists;
    Command List:- 
    1.) Create a new To-do list
    2.) Manage your tasks in an existing list
    3.) Manage your lists
    4.) Quit the program
    Type the command number in the terminal: """)
    if command == "1":
        create()
    elif command == "2":
        command_2 = input("""
        Task management Commands:-
        1.) Add a new task
        2.) Delete a task
        3.) Update a task
        Type the command number in the terminal: """)
        
        if command_2 == "1":
            add_task()
        elif command_2 == "2":
            delete_task()
        elif command_2 == "3":
            update_task()
    elif command == "3":
        command_2 = input("""
        List management Commands:-
        1.) Display the entire list
        2.) Delete a list
        Type the command number in the terminal: """)

        if command_2 == "1":
            read_list()
        elif command_2 == "2":
            delete()
    elif command == "4":
        exit()
