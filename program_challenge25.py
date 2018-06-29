def tester(pwd):
    if len(pwd) < 8:
        print ("The password \'" + pwd + "\' is a very weak password")
    elif len(pwd) > 8 and len(pwd) < 12:
        print("The password \'" + pwd + "\' is a weak password")
    elif len(pwd) > 12 and len(pwd) < 15:
        print("The password \'" + pwd + "\' is a weak password")    
    else:
        print("The password \'" + pwd + "\' is a very strong password")
    return(pwd)    
print ("*" *20 + "Password strength tester" + "*" *20)
password = raw_input("Please enter your password ")
test = tester(password)




       
