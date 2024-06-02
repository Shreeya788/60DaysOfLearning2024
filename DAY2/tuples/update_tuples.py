'''
we cannot change the value of tuple but we can change the values of list. 
That's why we use list() function to convert tuple to list. And change the values of list and convert it back to tuple.
'''


x = ("apple", "banana","cherry") # declaring a tuple 
y = list(x) #Converting tuple to list
y.append("orange") # adding element to list
x = tuple(y) # Converting list to tuple
print(x) # printing tuple