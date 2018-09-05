'''
Created on Feb 6, 2018

@author: ola
'''
import turtle,random

WIDTH = 0
HEIGHT = 0
SPACING = 10

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

def drawMany(num,size, oneFunc):
    
    turt = turtle.Turtle()
    turt.penup()
    turt.speed(0)
    turt.hideturtle()
    turt.sety(0)
    x = -WIDTH/2 + SPACING 
    cols = ["blue", "red", "yellow"]
    for count in range(num):
        turt.setx(x)
        #print("t at",turt.xcor(),turt.ycor())
        turt.color(cols[count % len(cols)])
        oneFunc(turt,size)
        x = x + size + SPACING
        


if __name__ == "__main__":
    
    # set up global state, WIDTH and HEIGHT
    # accessible as screen-size dimensions
    win = turtle.Screen()
    win.colormode(255)
    WIDTH = win.window_width()
    HEIGHT = win.window_height()
    
    # get number of drawables and create    
    size = 100
    num = WIDTH//(size + SPACING)   
    drawMany(num,size,drawSquare)
    win.exitonclick()
