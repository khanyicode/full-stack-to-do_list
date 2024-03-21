
from dashboard.tasks import view_tasks, add_task, delete_task

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