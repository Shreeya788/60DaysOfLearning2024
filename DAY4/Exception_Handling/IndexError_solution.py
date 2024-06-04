items = [1,2,3,4,5,6]

try:
    item = item[6]
    print(item)
except Exception as e:
    print("The index doesnot exist in the list")