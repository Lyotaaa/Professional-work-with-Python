from application.salary import calculate_salary
from application.application.db.people import get_employees
from datetime import date
from textual_datepicker import DateSelect

def show_date():
    t = date.today()
    print(t.strftime('Дата: %d.%m.%Y'))

if __name__ == "__main__":
    show_date()
    get_employees()
    calculate_salary()
    