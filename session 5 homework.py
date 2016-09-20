import turtle
import math
zhi = turtle.Turtle() 


def polygon(t, length, n):
    t.speed("fastest")
    t.lt(60)
    t.fd(length)
    t.lt(120)
    t.fd(length)
    t.lt(120)
    t.fd(length)
    for i in range(n):
        t.lt(30)
        t.fd(length)
        t.lt(120)
        t.fd(length)
        t.lt(120)
        t.fd(length)
    radius = length/math.sqrt(3) #Calculate radius of circle inside triangle
    t.penup()    
    t.goto(0,length-radius)
    t.goto(50,-90)
    t.pendown()       
    t.circle(102)

polygon(zhi, 100, 3)

turtle.mainloop()