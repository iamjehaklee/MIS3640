# def print_lyrics():
#     print("Hey Jude. Don't make it bad.")
#     print("Take a sad song and make it better.")

# # print_lyrics()
# # print(type(print_lyrics))

# def repeat_lyrics():
#     print_lyrics()
#     print('Na - na - na - na - na - na - na - na')
#     print_lyrics()

# # repeat_lyrics()

# def print_twice(Jerry):
#     print(Jerry)
#     print(Jerry)

# def cat_twice(a, b):
#     cat = a + b
#     print_twice(cat)

# line1 = 'Bind Tiddle'
# line2 = 'tiddle bang.'

# cat_twice(line1, line2)


# print(give_me_a_break())

# def my_abs(n):
#     if isinstance(n,int) or isinstance(n,float):
#         if n > 0:
#             return n
#         else:
#             return n 
#     else:
#         return "Invalid Value."

# print(my_abs('hi'))

#----------9/13/2016 - Exercise 1---------------

#ax^2 + bx + c=0 
import math

def quadratic(a,b,c):
    if isinstance(a,str) or isinstance(b,str) or isinstance(c,str):
        print("Please only use numbers.")
    else:
        if 4*a*c > b**2:
            print("The answers are imaginary. Please try again.")
        else:
            x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a) 
            x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a) 
            print('The two answers are', x1, 'and', x2, '.')       

print(quadratic(2,100,5))   #solvable 
print(quadratic(1,3,3))     #imaginary
