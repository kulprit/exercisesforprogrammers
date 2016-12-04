print("*" *10 + " Temperature Converter " + "*" * 10)

convert = raw_input("Press C to convert from Fahrenheit to Celsius.\nPress \
F to covert from Celsius to Farenheit.")

if convert == "C":
    print("your Choice: C")
    temp = int(raw_input("Please enter the temperature you wish to convert "))
    formulaC = (temp -32) * 5/9
    print("The temperature in Celsius is " + str(formulaC) + ".")           
elif convert == "F":
    print("Your Choice: F")
    temp = int(raw_input("Please enter the temperature you wish to convert "))
    formulaF = (temp * 9/5) + 32
    print("The temperature in Celsius is " + str(formulaF) + ".")               
else:
    print("You need to make a better choice between C and F")           
       

# try / except for non digits for input of temp
# functions
# GUI program
# also input kelvin temperatures
