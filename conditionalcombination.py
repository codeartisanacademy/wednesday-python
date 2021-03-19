paid = True
age = 12

# movie for older than 13 years old
if age > 13 and paid == True:
    print("You can watch the movie")
else:
    print("You can't watch the movie")

# movie for older than 13 years old
if age > 13 or paid == True:
    print("You can watch the movie")
else:
    print("You can't watch the movie")


