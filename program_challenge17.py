try:
    weight = int(raw_input("Enter your weight in pounds:"))
    height = int(raw_input("Enter your height in inches :"))
    gender = raw_input("Enter your gender :")
    volume = int(raw_input("Alcohol by volume in oz:"))
    time = int(raw_input("Time since last drink in hours:"))
    if gender == "Male":
        r = 0.73
    elif gender == "Female":
        r = 0.66
    else:
        print("Enter Male or Female")
             
    BAC = (volume * 5.14 / weight * r) - .015 * height

    print ("Your BAC is " + str(BAC))

    if BAC > 0.08:
        print("You should not drive")
    else:
        print("It is OK to drive")         
except:
    print("You need to enter the correct units")
             
#metric units
#BAC by state
# mobile application - update BAC by each drink - timer between each drink
# enter drink and get alcohol by volume?

