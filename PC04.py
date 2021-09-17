'''
Created on Sep 17, 2021
PC04
@author: Eli Jordan

This script draws random shapes with random colors, it gives me 80's tv background vibes

'''


from turtle import *
import random
import math
panel = Screen()
w = 600
h = 600
panel.setup(width=w, height=h)
panel.bgcolor('black')
colormode(255)



def randomColors():
    # returns a tuple of random rgb colors
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color

def draw_oct(turtle,r,fill):
    #func to draw an 8-sided polygon
    turtle.setheading(0)
    if fill == True:
        turtle.begin_fill()
        for i in range(1,9):
            turtle.left(45)
            turtle.forward(r)
        turtle.end_fill()
    elif fill == False:
        for i in range(1,r):
            turtle.left(45)
            turtle.forward(25)
            
def draw_rect(turtle,w,h,fill):
    #func to call rectangle drawing
    if fill == True:
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.end_fill()
    elif fill == False:
        turtle.setheading(0)
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        
def draw_triangle(turtle,r,fill):
    #draws an equilateral triangle
    if fill == True:
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.forward(r)
        turtle.left(120)
        turtle.forward(r)
        turtle.left(120)
        turtle.forward(r)
        turtle.end_fill()
    else:
        turtle.setheading(0)
        turtle.forward(r)
        turtle.left(120)
        turtle.forward(r)
        turtle.left(120)
        turtle.forward(r)
        
def turtleTeleport(turtle,location):
    #easily move turtle to different points
    turtle.up()
    turtle.goto(location[0],location[1])
    turtle.down()
    
def randomLocation():
    # generates a random x,y pair fit in the screen size
    location = (random.randint(-w/2,w/2),random.randint(-h/2,h/2))
    return location

trueFalse = [True, False]
shapes = Turtle()
lines = Turtle()
shapes.speed(0)
lines.speed(0)
for i in range(0,100):
    # I couldn't make my functions work with the turtle names
    shapes.pensize(random.randint(1,10))
    lines.pensize(random.randint(5,10))
    turtleTeleport(shapes,randomLocation())
    lines.color(randomColors())
    shapes.color(randomColors())
    draw_oct(shapes,random.randint(5,20),random.choice(trueFalse))
    turtleTeleport(shapes,randomLocation())
    shapes.color(randomColors())
    draw_triangle(shapes,random.randint(10,30), random.choice(trueFalse))
    lines.setheading(random.randint(0,360))
    turtleTeleport(lines,randomLocation())
    lines.forward(random.randint(10,50))
    turtleTeleport(shapes,randomLocation())
    shapes.color(randomColors())
    draw_rect(shapes,random.randint(10,40),random.randint(10,40), random.choice(trueFalse))








