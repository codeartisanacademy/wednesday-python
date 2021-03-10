# create a string
"This is a string"

'This is also a string'

'i can\'t do this' # escape using backslash

"This is a nice quote \"to be or not to be\" "

email = "john@gmail.com"

full_name = "John doe"
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
print('---')
print(full_name.find('doe'))

print(full_name.count('o'))

# check if a string start with something 
# this method return boolean (True or False)
print(full_name.lower().startswith("john"))
print(full_name.endswith("e"))

password = 'secret123'
print(password.isalpha()) # check if the string consists of letters
print(password.isnumeric()) # check if the string consists of numbers
print(password.isalnum()) # check if the string consists of letters & numbers

username = " wahyudi x  "
print(len(username))
clean_username = username.strip() # this will remove leading and trailing white spaces 
print(len(clean_username))

website = "http://google.com"

#print(website.index('x')) # find the character and return the index or error if not found
print(website.find('x')) # find the character and return the index or -1 if not found
