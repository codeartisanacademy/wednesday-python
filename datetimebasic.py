# import datetime module
import datetime

# get the current date and time
today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

# get the elements of date and time today.year
year = today.year
month = today.month
day = today.day

print(year)

# create your own date datetime.date
independence_day = datetime.date(year=1945, month=8, day=17)
print(independence_day)

# create your own time datetime.time()
lunch_time = datetime.time(hour=12, minute=30, second=0)
print(lunch_time)

# display weekday
print(today.weekday())

weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print(weekdays[today.weekday()])

# time delta
delta = today - independence_day
print(delta.days)
print(type(delta))

borrow_date = today
borrow_time = datetime.timedelta(weeks=1)
return_date = today + borrow_time
print(return_date)
print(borrow_time.total_seconds())

# datetime format
print(today)
# today date in format dd/mm/yyyy
print(today.strftime("%d/%m/%Y"))

# independence day in August 17, 1945
print(independence_day.strftime("%B %d, %Y"))

# create date time using strptime()
date_string = "2021/07/30"

date_object = datetime.datetime.strptime(date_string, "%Y/%m/%d")

print(date_object)

