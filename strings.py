# create a string
"This is a string"

'This is also a string'

'i can\'t do this' # escape using backslash

"This is a nice quote \"to be or not to be\" "

email = "john@gmail.com"

full_name = "john doe"
city = "JAKARTA"

# make it upercase, lowercase
print(full_name.upper())
print(city.lower())
print(full_name.title())

# index: the position of an object inside something
print(full_name[0])
print(full_name[2])

# exercise, print out the last letter in varible full name
print(full_name[-1]) # -1 will count the index backward
print(full_name[len(full_name)-1])

# to find characters
print(full_name.find('doe'))

print(full_name.count('o'))


