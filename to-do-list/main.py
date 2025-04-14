import json
import os

FILENAME = "./to-do-list/task.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    else:
        return []
    
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

tasks = load_tasks()

def show_menu():
    print("\n To-Do List Menu")
    print('1. View Tasks')
    print('2. Add task')
    print("3. Delete task")
    print('4. Exit')

def view_tasks():
    if not tasks:
        print("NO tasks found.")
    else:
        print("\n Your Tasks: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks()
    print("Task added.")

def delete_task():
    view_tasks()
    try: 
        index = int(input("Enter task number to delete: ")) -1
        if 0<=index<len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"deleted task: {removed}")
        else:
            print("Invalide Number")
    except ValueError:
        print("Enter a valid numver.")


while True:
    show_menu()
    choice = input("Enter your choice:")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice=="3":
        delete_task()

    elif choice == "4":
        print("Good bye! :)")
        break
    else:
        print("Invalid choice. Please try again.")