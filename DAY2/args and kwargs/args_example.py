'''
Args also known as Arbitary Arguments 
used as a parameter to pass any number of non-keyword variables
'''

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(4,5,6))
print(sum_of(2,3))