import math
gallon = 350

lshaped = raw_input("Is this an L shaped room? ")

if lshaped == "yes":
    length1 = raw_input("What is the length of room 1? ")
    width1 = raw_input("What is the widthof room 1? ")
    length = raw_input("What is the length of room 2? ")
    width = raw_input("What is the width of room 2? ")
    areal = (int(length1) * int(width1)) + (int(length) * int(width))
    cansl = int(areal)/gallon
    cansl_round = math.ceil(cansl)
    print "You will need " + str(cansl_round) + " cans to\
    cover\n " + str(areal) + " square feet"
else:    
    length = raw_input("What is the length? ")
    width = raw_input("What is the width? ")
    area = int(length) * int(width)
    cans = int(area)/gallon
    cans_round = math.ceil(cans)
    print "You will need " + str(cans_round) + " cans to cover\n " + str(area) + " square feet"

radius = raw_input("What is the radius? ")
area1 = 3.14 * (int(radius) * int(radius))
cans1 = int(area1)/gallon
round_cans = math.ceil(cans1)
print "You will need " + str(cans1) + " cans to cover\n " + str(area1) + " square feet"




