import math
dict = {'german': '80', 'french':'90', 'english':'70'}
country = raw_input("What country do you want to change to? ")
exchange = raw_input("How may euros are you changing? ")
rate = raw_input("What is the exchange rate? ")

if country == 'german':
    price = float(exchange) * float(rate) / float(dict['german'])
    price1 = float(math.ceil(price))
    print dict['german']
    print "You chose german and " +str(exchange) + " euros at a rate of " + str(rate) + " is\n" \
      + str(price1) + " U.S. dollars"
elif country == 'french':
    price = float(exchange) * float(rate) / float(dict['french'])
    price1 = float(math.ceil(price))
    print dict['french']
    print "You chose gfrench and " +str(exchange) + " euros at a rate of " + str(rate) + " is\n" \
      + str(price1) + " U.S. dollars"
else:
    price = float(exchange) * float(rate) / float(dict['english'])
    price1 = float(math.ceil(price))
    print dict['english']
    print "You chose english and " +str(exchange) + " pounds at a rate of " + str(rate) + " is\n" \
      + str(price1) + " U.S. dollars"


                     
