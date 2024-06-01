'''
Variable => changing value 
Naming convention of variable is of two types: 
    - Camel Case => First letter of the first word is lowercase and the first letter of every word 
    after that is uppercase with no spaces in between words
    Example: myName, yourName
    - Snake case => everything in lowercase letters but you use an underscore between words
    Example: my_name, variable_name
'''



x = 'abc'
print(x)

# After this variable value is reassigned 

x= '5'
print(x)

# variable can be deleted using del function 

del(x)

#now we check if its deleted or not using print function

print(x) # this statement throws error