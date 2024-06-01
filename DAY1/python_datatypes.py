'''
Data Type => an attribute associated with a piece of data that tells a computer system 
how to interpret its value

Five basic type of data in python are:
    - Numeric
        - Integer --> non-fractional positive or negative numbers
        - Float --> fractional numbers
        - Complex numbers --> imaginary and real numbers
    - Set --> enclosed by {} 
    - Dictionary --> enclosed by {} and value is stored in key-value pairs
    - Boolean --> True or False 
    - Sequence 
        - String  --> sequence of characters enclosed in single or double quotes
        - List --> enclosed by [] 
        - Tuple --> enclosed by () and the its value cannot be changed and modified
'''
a= [1, 'abc',0.004 ]
print(type(a))          # print <class 'list'>

b = 'John'
print(type(b))          #print <class 'str'>

c= {'a', 'b', 123}
print(type(c))          #print <class 'set'>

d = {'aa' :55, 'bb':59.4}
print(type(d))          #print <class 'dict'>