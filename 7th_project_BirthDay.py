import datetime
import time


def get_birthday():
    while True:
        try:
            year = int(input('insert the year of your next birthday'))
            month = int(input('insert the month of your next birthday'))
            day = int(input('insert the day of your next birthday'))
            if (0 <= year <= 9999) and (1 <= month <= 12) and (0 <= day <= 31):
                break
            else:
                print('this is invalid year')

        except ValueError:
            print('you have to insert numbers only')
    return datetime.datetime(year, month, day, 23, 59, 59)


def check_remaining_time():
    birth_day_date = get_birthday()
    while True:
        today = datetime.datetime.today()
        remaining_time = birth_day_date - today
        if datetime.timedelta(0) <= remaining_time <= datetime.timedelta(1):
            if remaining_time <= datetime.timedelta(0, 10):
                year = datetime.timedelta(365)
                birth_day_date = birth_day_date + year
            print('this is your birth day!!! for the next - ', remaining_time, 'hours')
            time.sleep(2)
        elif remaining_time < datetime.timedelta(0):
            print("this isn't your current birthday date")
            birth_day_date = get_birthday()
        elif remaining_time > datetime.timedelta(1):
            print(remaining_time - datetime.timedelta(1))
            time.sleep(2)


check_remaining_time()


