def find_factorial_by_recursion(n):
    if n==1 :
        return 1
    else: 
        return n*find_factorial_by_recursion(n-1)

print(find_factorial_by_recursion(5))