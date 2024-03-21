
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