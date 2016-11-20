first = raw_input("What is the first number?" )
second = raw_input("What is the second number? ")

firstint = int(first)
secondint = int(second)

add = firstint + secondint
sub = firstint - secondint
div = firstint / secondint
mul = firstint * secondint

print first + " + " + second + " = " + str(add)
print first + " - " + second + " = " + str(sub)
print first + " / " + second + " = " + str(div)
print first + " * " + second + " = " + str(mul)
