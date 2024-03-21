
from signup_.signup import *
from login_.login import *

tasks = []

def view_tasks():
    print("Tasks:")
    for task in tasks:
        print(task)

def add_task():
    task = input("Enter task: ")
    tasks.append(task)

def delete_task():
    task = input("Enter task to delete: ")
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found.")

def user_dashboard():
    print("Welcome to the Dashboard!")
    while True:
        choice = input("1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit to Main Menu\nChoose an option: ")

        if choice == "1":
            view_tasks()
            
        elif choice == "2":
            add_task()
            
        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Exiting the Dashboard.")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        choice = input("1. Signup\n2. Login\n3. Exit\nChoose an option: ")

        if choice == "1":
            signup()
            user_dashboard()
            
        elif choice == "2":
            login()
            user_dashboard()
            
        elif choice == "3":
            print("Exiting the app. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()