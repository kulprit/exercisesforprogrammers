import math
def calculateMonthsUntilPaidOff(bal, apr, monthly):
    time = -1/30*math.log(1+bal/monthly*(1-(1+apr/365)**30))/math.log(1+apr/365)
    time = bal *math.log(apr+monthly)
    return time

print ("*" *20 + "Pay off in months" + "*" *20)

balance = int(raw_input("What is your balance "))
apr1 = int(raw_input("What is the APR in months as a percentage" ))
month = int(raw_input("What is the monthly payment you can make: "))

func = math.ceil(calculateMonthsUntilPaidOff(balance, apr1, month))

print ("It will take you " + str(func) + "months to pay")                  


                  
                  
                  
