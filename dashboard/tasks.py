
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
        
        
def set_reminder():
    task_name = input("Enter task name to set a reminder: ")
    # Add code to set a reminder for the specified task

def update_task_status():
    task_name = input("Enter task name to update status: ")
    new_status = input("Enter new status for the task: ")
    # Add code to update the status of the specified task