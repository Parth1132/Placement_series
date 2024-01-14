def fibonacci(n):
    '''this function takes a number as the input and prints the relevant fibonacci series'''
    
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
print(fibonacci(5))