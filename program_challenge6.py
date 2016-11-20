import datetime
now = datetime.datetime.now()

current = raw_input("What is your current age? ")
retire = raw_input("What age would you like to retire? ")
summed = int(retire) - int(current)
date_retire = int(now.year) + int(summed) 

print "You have " + str(summed) + " years left until you can retire"

if summed < 0:
    print "You can retire now"
else:    
    print "It is %d " % now.year + " you can retire in " + str(date_retire)



