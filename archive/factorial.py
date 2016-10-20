# #1
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1) 

# print(factorial(5))

# #2 
# def fib(n):
#     if n == 1: 
#         return 1
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(8))

#3
def gcd(a, b):
    while b:
        c = a%b 
        a = b
        b = c
    return a
