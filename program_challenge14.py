amount = raw_input("What is the order amount? ")
state = raw_input("What is the state? ")

if state == 'WI':
    tax = 5.50
    totalTax = float(amount) * float(tax) / 100
    totalTax1 = round(float(totalTax),2)
    total = float(amount) + float(totalTax)
    total1 = round(float(total),2)
    amount1 = round(float(amount), 2)
    print "The order amount is $" + str(amount1)
    print "The tax is $" + str(totalTax1)
    print "The total is $" + str(total1)
else:
    amount2 = round(float(amount),2)
    print "The total is $" + str(amount2)
