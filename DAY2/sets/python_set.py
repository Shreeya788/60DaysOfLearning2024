'''
Set is a collection which is unordered, unchangeable and unindexed.

Sets are written with curly brackets and used to store multiple items in a single variable.

set is unchangeable but we can add new items or remove existing items from it.
it doesn't allow duplicate values

values True and 1 are considered same in set Likewise False and O are considered same

set() constructor can be used to make a set
'''
thisset = {"apple", "banana", "cherry","apple"}
print(thisset) #duplicate values are ignored

thisset1 = {"apple", "banana", "cherry", True,1,2}
print(thisset1) #treats True and 1 as same

print(len(thisset1)) #length of set
thisset3 = set(("mango", "strawberry", "cherry"))
print(thisset3) #set can be made using set() constructor