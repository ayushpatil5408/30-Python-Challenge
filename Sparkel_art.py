import turtle
import colorsys
import math
screen= turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.setworldcoordinates(-400,-300,400,300)
t= turtle.Turtle()
t.speed(0)
t.hideturtle()
a=0
while True:
    t.clear()
    for i in range(120):
        c=colorsys.hsv_to_rgb(i/120+a,1,1)
        t.color(c)
        angle=i*137.5
        r=i*3
        x=r* math.cos(math.radians(angle+a*200))
        y= r*math.sin(math.radians(angle+a*200))
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.goto(x,y)
        t.dot(8)
    screen.update()
    a+=0.02