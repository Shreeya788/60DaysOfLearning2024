class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.title}\nDescription: {self.description}\nStatus: {status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Added task: {title}")

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        print(f"Removed task: {title}")

    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f"Marked task as completed: {title}")
                return
        print(f"Task not found: {title}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        for task in self.tasks:
            print(task)

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add task\n2. Remove task\n3. Mark task as completed\n4. List tasks\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            title = input("Enter the title of the task to remove: ")
            todo_list.remove_task(title)
        elif choice == "3":
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.mark_task_as_completed(title)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            print("Exiting the to-do application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
