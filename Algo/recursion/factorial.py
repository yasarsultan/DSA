

# def fact(n):  
#     return 1 if (n==1 or n==0) else n * fact(n - 1)

num = int(input())

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
    
result = factorial(num)
print(result)
