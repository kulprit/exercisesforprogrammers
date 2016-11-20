newinput = raw_input("What is your name? ")

if len(newinput) == 0:
    print "You must enter a value!"
else:   
    print newinput + " your name has " + str(len(newinput)) + " letters"
