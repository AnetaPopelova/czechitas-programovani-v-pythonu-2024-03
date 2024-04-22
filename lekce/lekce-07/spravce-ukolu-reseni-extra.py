import uuid
import datetime
import logging

# Nastavení logování
logging.basicConfig(level=logging.INFO)

# Definice třídy Task, která reprezentuje úkol
class Task:
    def __init__(self, description, due_date=None, priority='Normal'):
        self.description = description
        self.timestamp = datetime.datetime.now()
        self.due_date = due_date
        self.priority = priority

# Třída pro správu úkolů
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description, due_date=None, priority='Normal'):
        task_id = uuid.uuid4()
        self.tasks[task_id] = Task(description, due_date, priority)
        logging.info(f"Task added with ID: {task_id}")
        return task_id

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            logging.info(f"Task {task_id} removed")
        else:
            logging.error("Task not found")

    def show_tasks(self, filter_keyword=None):
        for task_id, task in self.tasks.items():
            if filter_keyword is None or filter_keyword in task.description:
                print(f"{task_id}: {task.description} (Priority: {task.priority}) added on {task.timestamp}")
                if task.due_date:
                    print(f" Due by: {task.due_date}")

# Hlavní funkce aplikace
def main():
    manager = TaskManager()
    while True:
        command = input("Enter command (add, remove, show, exit): ")
        if command == 'add':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD), or leave blank if none: ")
            priority = input("Enter priority (Low, Normal, High): ")
            manager.add_task(description, due_date if due_date else None, priority)
        elif command == 'remove':
            task_id = input("Enter task ID to remove: ")
            manager.remove_task(uuid.UUID(task_id))
        elif command == 'show':
            filter_keyword = input("Enter keyword to filter by, or just press enter to show all: ")
            manager.show_tasks(filter_keyword if filter_keyword else None)
        elif command == 'exit':
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
