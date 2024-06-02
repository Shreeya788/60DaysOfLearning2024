# add()method is used to add one item in set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") 
print(thisset)

# Add items from another set into the current ser using update() method

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove item from set using remove() method or discard() method

thisset.remove("banana")
print(thisset)

#discard() method will remove the item if it is present in the set, otherwise it will do nothing

thisset.discard("orange")
print(thisset)

#pop() method removes an random item from the set

thisset.pop()
print(thisset)