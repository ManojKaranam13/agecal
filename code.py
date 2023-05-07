from datetime import date
def calculate_age(day, month, year):
    today = date.today()
    birthdate = date(year, month, day)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
day=int(input("enter the day"))
month=int(input("enter the month"))
year=int(input("enter the year"))
print(calculate_age(day,month,year))

