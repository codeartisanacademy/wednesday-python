email = input("enter your email address: ")

# valid email john@gmail.com
# invalid email jo.hn@gmail

if email != "":
    # check if the email address has @ character
    if email.count("@") == 1:
        index_atsign = email.find('@') # return the index (position) or -1
        dot = email.find('.', index_atsign)
        if dot != -1:
            print("email is valid")
        else:
            print("email is not valid")
    else:
        print("email is not valid")
else:
    print("Please enter an email address")