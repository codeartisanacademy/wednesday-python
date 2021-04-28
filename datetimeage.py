import datetime

# ask for year
year = input("Enter your birth year: ")
# ask for month
month = input("Enter your birth month: ")
# ask for day
day = input("Enter your birth day: ")

# print out "You are x years old."
birth_date = datetime.date(year=int(year), month=int(month), day=int(day))

today = datetime.date.today()

age = today - birth_date

print(round(age.days/365))

# you have been living in this world for x days
# your were born on x 