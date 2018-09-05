'''
Created on Feb 1, 2018

@author: ola
'''
import turtle, random

WIDTH = 0
HEIGHT = 0

def changeTurtle(turt):
    """
    Modify turt, a turtle, to be a "random" turtle with
    a random color and a random position
    for the turtle.
    
    Return the turtle (the turtle is modified
    even if return value ignored on call)
    """
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
 
    turt.penup()
    turt.hideturtle()
    turt.speed(0)
    turt.color(r,g,b)
    
    # (x,y) are somewhere on the screen, all points
    # equally likely
    
    x = random.randint(-WIDTH/2,WIDTH/2)
    y = random.randint(-HEIGHT/2,HEIGHT/2)
 
    turt.setposition(x,y)

    return turt

def drawOneSquare(turt,size):
    """
    Create a square of the specified size
    using turtle's color and coordinates
    
    Parameter turt is a turtle and parameter
    size is the size of the square drawn (float)
    """
    turt.begin_fill()
    
    for _ in range(4):
        turt.forward(size)
        turt.right(90)
    
    turt.end_fill()

def drawMany(num):
    """
    draw as many random shapes as specified by
    the value of int parameter num
    
    Calls drawOneSquare num times as currently written
    """
  
    ola = turtle.Turtle()
    for _ in range(num):
        ola = changeTurtle(ola)
        drawOneSquare(ola,random.randint(40,80))

if __name__ == '__main__':
    # set up global state, WIDTH and HEIGHT
    # accessible as screen-size dimensions
    win = turtle.Screen()
    win.colormode(255)
    WIDTH = win.window_width()
    HEIGHT = win.window_height()
    
    # get number of drawables and create
    num = input("number of elements> ")
    num = int(num)
    drawMany(num)
    win.exitonclick()