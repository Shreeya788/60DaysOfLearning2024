# Lambda Function are small arguments which can take any number of arguments but can have only one expression

def my_func(n):
    return lambda a : a*n
my_doubler = my_func(2)
print(my_doubler(11))