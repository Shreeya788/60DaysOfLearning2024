list1 = [1,2,3,4,5]
# print(*list1)  // prints entire lists
print(list1,sep=" ")
# list1.insert(len(list1),6)  # used to insert elements in list1
# list1.append(6) # used to add elements in list
list1.extend([6,7,8,9])  # used to extend list to given element

print(list1,sep=" ")
list1.pop(8) # used to remove elements of 8th index that is 9
print(list1,sep=" ")

del list1[2] # used to delete specified element of the index in the list
