'''
Dictionaries are used to store data values in key-value pairs.
A dictionary is a collection of ordered, changeable and do not allow duplicate values(as per python 3.7)


'''

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)

#dictionary items can be referred using key name
print(thisdict["brand"])

#dictionary can be defined using dict() constructor

thisdict_1 = dict(name="John", age = 25, country = "Nepal")
print(thisdict_1)