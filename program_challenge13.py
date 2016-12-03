import math

amount = raw_input("What is the principle amount? ")
rate = raw_input("What is the rate? ")
years = raw_input("What is the number of years? ")
times = raw_input("What is the number of times the interest\nis compunded per year? ")

times1 = float(times)
multiply = float(years) * float(times1)
divide = float(rate)/ float(years)
compound = (float(amount)* (1+float(divide)))
compound1 = compound ** multiply
print multiply

print str(amount) + " invested at " + str(rate) + " for " + str(years)\
     + " years compounded " + str(times1) + " times per year is $" + str(compound1)                     

##calculation is wrong
