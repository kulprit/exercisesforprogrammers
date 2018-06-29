first = int(raw_input("Enter the first number: "))
second = int(raw_input("Enter the second number: "))
third = int(raw_input("Enter the third number: "))

if first > second and first > third:
    print ("The largest number is" + str(first))
elif second > third and second > first:
    print ("The largest number is" + str(second))
else:
    print ("The largest number is " + str(third))


#store all values entered and error if a duplicate is typed
# ask for 10 numbers
# ask for unlimited - Q to quit and review

