'''
Created on Feb 6, 2018

@author: ola
'''

import turtle

def drawCircle(turtle,size):
    """
    Create a circle with specified radius
    Use turtle's position to create circle
    When finished turtle pen will be up
    """
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()

def drawSquare(turtle,size):
    """
    Create square of specified size, by
    turning right.
    Use turtle's position and color
    When finished turtle will be up
    """
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        
    turtle.end_fill()
    turtle.penup()
 
def drawOneSnowy(t1,radius):
    """
    create a snowperson using the turtle t1
    that's a parameter for position
    
    leaves turtle hidden at end
    BUGBUG: should turtle be at same position when done?
    """

    t1.color("red")
    drawCircle(t1,radius)
    
    t1.color("blue")
    t1.setposition(t1.xcor(),t1.ycor()+2*radius)
    radius = radius//2
    drawCircle(t1,radius)
    
    t1.color("green")
    t1.setposition(t1.xcor(),t1.ycor()+2*radius)
    radius = radius//2
    drawCircle(t1,radius)
    
    t1.hideturtle()   
    
if __name__ == '__main__':
    win = turtle.Screen()
    #drawManyRandom()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setposition(-80,0)
    drawOneSnowy(t,100)
    t.setposition(80,50)
    drawOneSnowy(t,60)
    win.exitonclick()