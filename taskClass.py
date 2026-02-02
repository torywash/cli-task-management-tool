""" Class file for a Task object in the Task Manager application. """
# task class definition
class Task:
    # initialize task attributes
    def __init__(self, name, date, time, meridiem, priority, description):
        self.name = name
        self.date = date
        self.time = time
        self.meridiem = meridiem
        self.priority = priority
        self.description = description

    # string representation of the task
    def __repr__(self):
        return (f"Name: {self.name}, Priority: {self.priority}, Date: {self.date}, Time: {self.time}, Meridiem: {self.meridiem}, Description: {self.description}")