from application.salary import calculate_salary
from application.application.db.people import get_employees
from datetime import datetime

def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("CUrrent Time: ", current_time)

if __name__ == "__main__":
    current_time()
    get_employees()
    calculate_salary()