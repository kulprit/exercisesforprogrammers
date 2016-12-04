print ("*" * 10 + " BMI Calculator " + "*" * 10)
height = float(raw_input("Enter your height in feet and inches "))
weight = int(raw_input ("Enter your weight in lbs "))
adjusted_height = height * 12
print(adjusted_height)
bmi = (weight/(adjusted_height * adjusted_height))*703
print ("Your BMI is " + str(bmi))
if bmi <= 18.4:
    print ("You are underweight")
elif bmi <= 25:
    print ("You are in the ideal range")
else:
    print ("You are overweight go see a doctor")
        

