import turtle

jerry = turtle.Turtle()

# print(jerry)

# jerry.fd(100)
# jerry.fd(100)
# jerry.lt(90)
# jerry.fd(100)
# jerry.fd(100)
# jerry.lt(90)
# jerry.fd(100)
# jerry.fd(100)
# jerry.lt(90)
# jerry.fd(100)
# jerry.fd(100)

# turtle.mainloop()

# for i in range(4):
#     print('hello')

#Class Session 5 Number 1 and 2
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

Jerry = turtle.Turtle()

square(Jerry,100)

#Class Session 5 Number 3

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

num1 = turtle.Turtle()
# polygon(num1,20,20)

# num2 = turtle.Turtle()
# polygon(num2,10,4)

# turtle.mainloop()


# Exercise 2.4
import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

# circle(num1, 100)
turtle.mainloop()

def polyline(t, n, length, angle,x):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        t.tilt(360/x)
polyline(Jerry, 2, 100, 9)

