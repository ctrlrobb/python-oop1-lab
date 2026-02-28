from datetime import datetime

def validate_task_title(title):
    if len(title) > 0:
        return True
    print("Error: Title cannot be empty.")
    return False
    
def validate_task_description(description):
    if len(description) > 0:
        return True
    return False    
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Invalid date format.")
        return False