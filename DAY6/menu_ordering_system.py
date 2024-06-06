menu = {
    1: {
        "name" : "espresso",
        "price" : 1.99
    },
    2: {
        "name" : "coffee",
        "price" : 2.50
    },
    3:{
        "name" : "cake",
        "price" : 2.79
    },
    4: {
        "name" : "soup",
        "price" : 4.50
    },
    5:{
        "name" : "sandwich",
        "price" : 4.99
    }
}
def calculate_subtotal(order):
    print('Calculating tax from subtotal...')
    subtotal = sum(item['price'] for item in order)
    return subtotal


def calculate_tax(subtotal):
    tax = round(subtotal * 0.15,2)
    return tax

def summarize_order(order):
    names = [items["name"] for items in order]
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax,2)
    return names, total

    
def take_order():
    display_menu()
    order =[]
    count = 1
    for _ in range(3):
        items = input('Select menu item number ' + str(count) + '(from 1 to 5): ')
        count +=1
        order.append(menu[int(items)])
    return order



def display_menu():
    print("-------- Menu -------")
    for selection in menu:
        print(f"{selection}.{menu[selection]['name'] : <9} | {menu[selection]['price'] : >5} ")
    print()
def print_order(order):
    print("You have ordered "+ str(len(order)) + ' items ')
    items =[]
    items =[item["name"] for item in order]
    print(items)
    return order
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is : " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is : " + str(tax))

    items,total = summarize_order(order)
    print("Order summary:", items)
    print("Total cost:", total)

if __name__== '__main__':
    main()