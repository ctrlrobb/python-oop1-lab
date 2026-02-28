from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        tasks.append({
            "title": title, 
            "description": description, 
            "due_date": due_date, 
            "completed": False
        })
        print("Task added successfully!")

def mark_task_as_complete(index):
    try:
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    except (IndexError, TypeError):
        print("Error: Invalid task index.")

def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    for task in pending:
        print(f"Title: {task['title']}")

def calculate_progress():
    if len(tasks) == 0:
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100