age = int(input('How old are you?'))

if age >= 21:
    print("Your age is " + str(age) + '.')
    print('Yes, you can.')
elif age >= 6:
    print("Your age is " + str(age) + '.')
    print("Teenager.")
else:
    print("Your age is " + str(age) + '.')
    print('No, not allowed.')
#--------------------------------------------
# x=1
# y=2

# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')
#--------------------------------------------

#Exercise 1 
# weight = int(input('Please enter your weight in pounds:'))
# height = int(input('Please enter your height in inches:'))

# BMI = 703 * weight / height**2 

# if BMI >= 30:
#     print('Your BMI is ' + str(BMI) + '.')
#     print('You are obese.')
# elif BMI < 30 and BMI >= 25:
#     print('Your BMI is ' + str(BMI) + '.')
#     print('You are overweight.')
# elif BMI < 25 and BMI >= 18.5: 
#     print('Your BMI is ' + str(BMI) + '.')
#     print('You are normal weight.')
# else: 
#     print('Your BMI is ' + str(BMI) + '.')
#     print('You are underweight.')
#--------------------------------------------

#Exercise 2 
# varA = input('Please input something:')
# varB = input('Please input something else:')

# if str.isdigit(varA) == True and str.isdigit(varB) == True:
#     if varA > varB:
#         print("bigger")
#     elif varA < varB:
#         print("smaller")
#     else: 
#         print('equal')
# else:
#     print('strings involved')

#--------------------------------------------
# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
# countdown(4)
#--------------------------------------------
# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print('n = ', n)
#     print_n(s, n-1)

# print_n('hello', 3)