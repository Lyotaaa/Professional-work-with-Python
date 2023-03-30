import time

def get_employees():
    time_loc = time.localtime()
    current_time = time.strftime("%H:%M:%S", time_loc)
    print(current_time)
