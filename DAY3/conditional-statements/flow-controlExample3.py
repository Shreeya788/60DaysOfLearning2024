loyalty_customer = True
total_bill = 95

if loyalty_customer and total_bill >100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/100)* 20
elif total_bill>100 :
    #give 10% discount
    total_bill = total_bill- (float(total_bill)/100)*10
else:
    #sorry no discount, 5% service charge is applied
    print("Sorry, no discount...")
print("Total bill: ", float(total_bill))