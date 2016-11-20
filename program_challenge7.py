constant = 0.09290304

length = raw_input("What is the length of the room in feet? ")
width = raw_input("What is the length of the room in feet? ")

area = int(length) * int(width)
meter_area = float(area) * constant

print " You entered dimensions of " + length + " feet by " + width + " feet."
print "The area is"
print str(area) + " square feet"
print str(meter_area) + " square meters"
