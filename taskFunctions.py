""" Functions file for task manager"""
# imports
import taskClass
import taskFunctions
import time
import json
import os

# functions

    # open JSON and load items
def load_tasks():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(f'{current_dir}/tasks.json', 'r') as file:
            tasks_data = json.load(file)
            tasks_data = [taskClass.Task(**task_dict) for task_dict in tasks_data]
    except (FileNotFoundError, json.JSONDecodeError):
        tasks_data = []
    return tasks_data

    # announce what is due today
def daily_announcement(tasks):
    from datetime import datetime
    today = datetime.now().strftime("%m-%d-%Y")
    due_today = [task for task in tasks if task.date == today]
    if due_today:
        print("Tasks due today:")
        for task in due_today:
            print(task)
        time.sleep(len(due_today))
    else:
        print("No tasks due today.")
        time.sleep(0.5)

    # get the task details
def get_task():
    try:
        name = input("Enter task name: ")
        date = input("Enter task date (MM-DD-YYYY): ")
        time = input("Enter task time (HH:MM): ")
        meridiem = int(input("1) AM \n2) PM \nSelect an Option (1-2): "))
        if meridiem == 1:
            meridiem = "AM"
        elif meridiem == 2:
            meridiem = "PM"
        else:
            print("Invalid option selected. Defaulting to AM.")
            meridiem = "AM"
        priority = input("Enter task priority (Low, Medium, High): ")
        description = input("Enter task description: ")
        return (name, date, time, meridiem, priority, description)
    except Exception as e:
        print(f"Error getting task details: {e}")
        return None

    # schedule the task
def schedule_task(name, date, time, meridiem, priority, description):
    try:
        task = taskClass.Task(name, date, time, meridiem, priority, description)
        print("Task scheduled successfully:")
        print(task)
    except Exception as e:
        print(f"Error scheduling task: {e}")

    # edit task details
def update_task(task, name=None, date=None, time=None, meridiem=None, priority=None, description=None):
    try:
        if name:
            task.name = name
        if date:
            task.date = date
        if time:
            task.time = time
        if meridiem:
            task.meridiem = meridiem
        if priority:
            task.priority = priority
        if description:
            task.description = description
        print("Task updated successfully:")
        print(task)
    except Exception as e:
        print(f"Error updating task: {e}")

    # edit task details
def edit_task(tasks_data):
    try:
        if not tasks_data:
                print("No tasks to edit.")
        else:
            for idx, task in enumerate(tasks_data, start=1):
                print(f"{idx}) {task}")
            print(f"{idx+1}) Cancel")
            task_idx = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_idx < len(tasks_data):
                name = input("Enter new task name (leave blank to keep current): ")
                date = input("Enter new task date (MM-DD-YYYY) (leave blank to keep current): ")
                time = input("Enter new task time (HH:MM) (leave blank to keep current): ")
                meridiem = input("Enter new task meridiem (AM/PM) (leave blank to keep current): ")
                priority = input("Enter new task priority (Low, Medium, High) (leave blank to keep current): ")
                description = input("Enter new task description (leave blank to keep current): ")
                
                # update task details
                update_task(tasks_data[task_idx], 
                            name=name if name else tasks_data[task_idx].name, 
                            date=date if date else tasks_data[task_idx].date, 
                            time=time if time else tasks_data[task_idx].time, 
                            meridiem=meridiem if meridiem else tasks_data[task_idx].meridiem,
                            priority=priority if priority else tasks_data[task_idx].priority, 
                            description=description if description else tasks_data[task_idx].description)

                # save task
                taskFunctions.save_tasks(tasks_data)

            elif task_idx == len(tasks_data):
                print("Edit cancelled, returning to menu.")

            else:
                print("Invalid task number. Please try again.")
                edit_task(tasks_data)
    except Exception as e:
        print(f"Error editing task: {e}")

    # view tasks
def view_tasks(tasks_data):
    try:
        if not tasks_data:
            print("\nNo tasks scheduled.")
            
            # choose viewing method
        else:
            view_choice = int(input("\n1) View All Tasks \n2) View By Priority \n3) View By Dates \n4) Return to Menu \nSelect an Option (1-4): "))

                # handling view choices
                # all tasks
            if view_choice == 1:
                print("\nAll Tasks:")
                for idx, task in enumerate(tasks_data, start=1):
                    print(f"{idx}) {task}")
                time.sleep(1)  # sleep for cleaner output
                
                # by priority
            elif view_choice == 2:
                print("\nTasks by Priority:")
                tasks_data.sort(key=lambda x: {'High': 1, 'Medium': 2, 'Low': 3}[x.priority])
                for idx, task in enumerate(tasks_data, start=1):
                    print(f"{idx}) {task}")
                time.sleep(1)  # sleep for cleaner output
                
                # by dates
            elif view_choice == 3:
                print("\nTasks by Upcoming Dates:")
                tasks_data.sort(key=lambda x: (x.date, x.time))
                for idx, task in enumerate(tasks_data, start=1):
                    print(f"{idx}) {task}")
                time.sleep(1)  # sleep for cleaner output

                # return to menu
            elif view_choice == 4:
                print("Viewing cancelled, Returning to menu.")

                # else
            else:
                print("Invalid option selected. Please try again.")
                view_tasks(tasks_data)
    except Exception as e:
        print(f"Error viewing tasks: {e}")

    # delete task
def delete_task(tasks_data):
    try:
        if not tasks_data:
                print("No tasks to delete.")
        else:
            for idx, task in enumerate(tasks_data, start=1):
                print(f"{idx}) {task}")
            print(f"{idx+1}) Cancel")
            task_idx = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_idx < len(tasks_data):
                deleted_task = tasks_data.pop(task_idx)
                print(f"Deleted task: {deleted_task}")
                taskFunctions.save_tasks(tasks_data)
            elif task_idx == len(tasks_data):
                print("Deletion cancelled.")
            else:
                print("Invalid task number. Please try again.")
                delete_task(tasks_data)
    except Exception as e:
        print(f"Error deleting task: {e}")

    # save tasks to JSON
def save_tasks(tasks):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(f'{current_dir}/tasks.json', 'w') as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)
        print("Tasks saved to tasks.json")
    except Exception as e:
        print(f"Error saving tasks: {e}")