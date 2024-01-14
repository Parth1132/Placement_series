def factorial(n):
    '''this functions take a number n as input and prints the factorial'''
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))