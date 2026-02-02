""" Task manager module to handle scheduling and execution of tasks. """
# imports
import taskClass
import taskFunctions

# open JSON to store and read tasks
tasks_data = taskFunctions.load_tasks()

# daily announcements
taskFunctions.daily_announcement(tasks_data)

# menu loop
while True:
    
    # display menu
    print("\nTask Manager Menu:")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Edit Task")
    print("4) Delete Task")
    print("5) See Today's Announcements")
    print("6) Exit")
    choice = input("Select an option (1-6): ")
    
    # handle choices
    # add task
    if choice == '1':
        details = taskFunctions.get_task()
        taskFunctions.schedule_task(*details)
        tasks_data.append(taskClass.Task(*details))
        taskFunctions.save_tasks(tasks_data)
    
    # view tasks
    elif choice == '2':
        taskFunctions.view_tasks(tasks_data)

    # edit task
    elif choice == '3':
        taskFunctions.edit_task(tasks_data)
    
    # delete task
    elif choice == '4':
        taskFunctions.delete_task(tasks_data)

    # today's announcements
    elif choice == '5':
        taskFunctions.daily_announcement(tasks_data)

    # exit
    elif choice == '6':
        taskFunctions.save_tasks(tasks_data)
        print("Exiting Task Manager. Goodbye!")
        break
    
    # invalid choice
    else:
        print("Invalid choice. Please select a valid option.")