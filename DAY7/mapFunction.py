coffees = ['Espresso','Latte','Cappuccino','Machhiato','Americano','Decaf']

def reverse_str(str):
    return str[::-1]
reversed_coffees = map(reverse_str,coffees)
for x in reversed_coffees:
    print(x)

