def func_divide(a,b):
    print (a/b)

try:
    ans = func_divide(40,0)
except ZeroDivisionError as e:
    print(e, "We cannot divide number by zero!!")
except Exception as e:
    print(e,"Something went wrong!!")
