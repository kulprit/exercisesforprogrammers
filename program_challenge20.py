import math

print ("*" * 20 + " Multistate Sales Tax Calculator " + "*" * 20)

amount = raw_input("What is the order amount? ")
state = raw_input("What state do you live in? ")

if state == "New York":
    result = float(amount) * 0.05
    total = float(amount) + result
    print("The tax rate is $" + str(result)+"\nThe total is $" + str(total))
else:
    result = float(amount) * 0.08
    total = float(amount) + result   
    print ("Default rate is $" + str(result)+"\nThe total is $" +  str(total))      
       
       
#format result to 2 decimal places
##math.ceil
##support for state and counties
##state abbreviations
##full state in upper/lowrr/mixed case
##avoid nested if's
    
