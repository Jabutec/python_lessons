tasks = [
    {"task": "Buy groceries", "priority": "medium", "done": False},
    {"task": "Finish Python project", "priority": "high", "done": False},
]

def add_tasks(tasks, task_name, priority):
    new_task = {"task": task_name, "priority": priority, "done": False}
    tasks.append(new_task)
    
    return True

def view_tasks(tasks):
    for task in tasks:
        print(f"Task: {task['task']}")
        print(f"Priority: {task['priority']}")
        print(f"Done: {task['done']}")
    

def find_tasks(tasks, task_name):
    for task in tasks:
        if task_name.lower() == task['task'].lower():
            return task
    return None

def complete_task(tasks, task_name):
    task = find_tasks(tasks,task_name)
    if task:
        task["done"] = True
        print(f"{task['task']} marked as done")
        return True
    return False

def delete_task(tasks, task_name):
    task = find_tasks(tasks, task_name)

    if task:
        tasks.remove(task)
        return True

    return False

while True:
    print("\nContact Menu:")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Find tasks")
    print("4. Complete Tasks")
    print("5. Delete tasks")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        task_name = input("Enter the name of the task: ").strip()
        priority = input("Enter the level of priority(medium, high or low): ").strip().lower()
        
        result = add_tasks(tasks, task_name, priority)
        if result:
            print("Task added successfully!")
    
    elif choice == "2":
        view_tasks(tasks)
        
    elif choice == "3":
        task_name = input("Enter the name of the task: ").strip()
        task = find_tasks(tasks, task_name)
        
        print(task)
    
    elif choice == "4":
        task_name = input("Enter the name of the completed task: ").strip()
        result = complete_task(tasks, task_name)
        
        if not result:
            print("Task not found")
    
    elif choice == "5":
        task_name = input("Enter the name of the task: ").strip()
        result = delete_task(tasks, task_name)
        
        if not result:
            print("Task not found")
            
    elif choice == "6":
        print("Exiting....")
        break 
    
    else:
        print("Invalid input")