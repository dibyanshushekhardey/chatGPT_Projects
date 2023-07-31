class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task marked as complete!")
        else:
            print("Task not found!")

    def display_tasks(self):
        if self.tasks:
            print("Todo List:")
            for task in self.tasks:
                print("- " + task)
        else:
            print("Todo List is empty!")

def main():
    print("Welcome to Todo List!")
    todo_list = TodoList()

    while True:
        print("\nAvailable Options:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to mark as complete: ")
            todo_list.complete_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Thank you for using Todo List!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
