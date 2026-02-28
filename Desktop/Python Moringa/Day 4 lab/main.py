import sys

# Mapping the flat structure to the expected package path
import task_utils as task_utils
sys.modules['task_manager'] = sys.modules[__name__]
sys.modules['task_manager.task_utils'] = task_utils

from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(input("Title: "), input("Desc: "), input("Date (YYYY-MM-DD): "))
        elif choice == "2":
            try:
                idx = int(input("Enter task number to complete: ")) - 1
                mark_task_as_complete(idx)
            except ValueError:
                print("Enter a number.")
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            print(f"Progress: {calculate_progress()}%")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()