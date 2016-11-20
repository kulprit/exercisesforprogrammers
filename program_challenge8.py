people = raw_input("How many people do you have? ")
pizza = raw_input("How many pizza's do you have? ")

slices = int(pizza) * 8

person_slice = int(slices) / int(people)
leftover = int(slices) % int(people)

print people + " people with " + str(pizza) + " pizzas"
print "Each person gets " + str(person_slice) + " of pizza"
print "There are " + str(leftover) + " peices"


