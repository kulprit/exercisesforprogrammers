import getpass

p = getpass.getpass()
print "you entered: ", p
user = raw_input("What is the user name? ")

if user == "sean":
    print "Hello Sean"
    password = raw_input("What is the password? ")
    if password == "12345":
        print "Welcome"
    else:
        print "I dont know you"
else:
    print "I dont know you"


