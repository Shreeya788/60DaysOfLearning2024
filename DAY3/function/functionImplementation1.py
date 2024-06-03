def calculate_tax(bill,tax_rate):
    total_tax = (bill*tax_rate) /100;
    return total_tax
print('Total Tax is : ',calculate_tax(175.00,15)) 
print('Total Tax is : ',calculate_tax(164.33,22)) 