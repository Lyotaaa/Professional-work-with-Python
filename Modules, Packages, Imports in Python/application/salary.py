from datetime import datetime
import pytz

def calculate_salary():
    time_MO = pytz.timezone('Europe/Moscow')
    datetime_MO = datetime.now(time_MO)
    print("Time:", datetime_MO.strftime("%H:%M:%S"))