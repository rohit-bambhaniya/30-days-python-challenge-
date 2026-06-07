

class ToDoApp:

    def __init__(self):
        self.task = []

    def add_task(self):

        add_task = input("Enter your task:").strip()

        if not add_task:

            print("Input cannot be empty!")
            return

        self.task.append(add_task)
        
        print("Task added successfully!")

    
    def view_task(self):

        if not self.task:

            print("Your To-Do list is empty!")
            return
        
        print("\n---- Your task ----")

        for i,t in enumerate(self.task, start=1):

            print(f"{i}.{t}")

    def remove_task(self):

        try:

            task_number = int(input("Enter index delete task :-"))

            delete_task = task_number - 1

            if delete_task < 0 or delete_task >= len(self.task):

                print("Invalid task number! Please check the list again.")
                return

            deleted_task = self.task.pop(delete_task)

            print(f"Task deleted: {deleted_task}")
        
        except ValueError:

            print("Enter valid value!")

    

def main():

    todo = ToDoApp()

    print("=== ToDoApp ===")

    while True:

        print("""
        1.Add Task
        2.view Task
        3.Remove Task
        4.Exit
        """)

        choice_task = input("Choice your Task:-")

        if choice_task == '1':
            todo.add_task()

        elif choice_task == '2':
            todo.view_task()

        elif choice_task == '3':
            todo.remove_task()

        elif choice_task == '4':
            print("Exit")
            break

        else:

            print("Invalid choice!")
        
        




if __name__ == "__main__":
    main()
