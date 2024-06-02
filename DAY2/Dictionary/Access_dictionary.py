'''
Dictionary can be accessed using its key name inside the square brackets
'''
thisdict = {"brand": "Ford", "model": "Mustang", "year":1964}
 
x= thisdict["model"]
print(x)    #returns the value of model

#get method can be used to obtain value
# this works exactly like the above method

y= thisdict.get("model")
print(y)

#getting keys using keys()method
key= thisdict.keys()
print(key)

#getting values of dictionary using values()
values = thisdict.values()
print(values)