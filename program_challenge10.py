tax = 5.5
item1 = raw_input("Enter the price of item 1 ")
quant1 = raw_input("Enter the quanity of item 1 ")
item2 = raw_input("Enter the price of item 2 ")
quant2 = raw_input("Enter the quanity of item 2 ")
item3 = raw_input("Enter the price of item 3 ")
quant3 = raw_input("Enter the quanity of item 3 ")

sub = (float(item1) * float(quant1)) + (float(item2) * float(quant2)) +(float(item3) + float(quant3))
sub1 = round(sub,2)

tax = sub * tax /100
tax1 = round(tax,2)

total = sub + tax
total1 = round(total,2)

print "Subtotal: $"+ str(sub1)
print "Tax: $"+ str(tax1)
print "Total: $"+ str(total1)    
    
