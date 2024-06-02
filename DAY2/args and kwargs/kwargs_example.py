'''
Kwargs also known as Arbitary keyword Arguments
used as parameter to pass any amount of keyword arguments
'''

def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return sum
print(sum_of(coffee= 3.5, tea = 6.8))