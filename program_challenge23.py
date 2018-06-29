car = raw_input("Is the car silent when you turn on the key: ")
if car == 'n':
    battery = raw_input("Are the battery terminals corroded: ")
    if battery == 'y':
        print("clean terminals and try again")
    else:
         print("replace the cables and try again")
else:
    click = raw_input("Does the car make a clicking noise?")
    if click == 'y':
        print("Replace the battery")
    else:
        crank = raw_input("Does the car crank up but fail to start?")
        if crank == 'y':
            print("Check the spark plugs")
        else:
            die = raw_input("Does the engine start and die?")
            if die == 'y':
                inject == raw_input("Does your car have fuel injection")
                if inject == 'y':
                    print ("Get it in for service")
                else:
                    print("Check to ensure the choke is opening and closing")
            else:
                print("The car is buggered")

# rules engine and inference engine - pyke - to be reviewed
                
