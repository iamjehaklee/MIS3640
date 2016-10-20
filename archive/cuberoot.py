# x = int(input('Enter an integer: '))
# ans = 0

# if x < 0:
#     while ans**3 < -x:
#         ans = ans + 1
#     if ans**3 != -x:
#         print(str(x) + ' is not a perfect cube')
#     else:
#         print('Cube root of ' + str(x) + ' is ' + str(-ans))
# else:
#     while ans**3 < x:
#         ans = ans + 1
#     if ans**3 != x:
#         print(str(x) + ' is not a perfect cube')
#     else:
#         print('Cube root of ' + str(x) + ' is ' + str(ans))

#------------------------------

cube = 62
epsilon = 0.0001
guess = 0.0
increment = 0.00001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)


# try with cube = 27, and large step (e.g. 2.0)