'''
Created on Feb 6, 2018

@author: ola
'''
import turtle
import SimpleTurtleShapes

SPACING = 10

def drawMany(num,size, ycoord):
    """
    draw many shapes (e.g., snowpeople or circles)
    in a single row.
    
    num is how many shapes in the row
    size is the size of each shape
    ycoord is the base of the y-coordinate of each shape drawn
    """
    turt = turtle.Turtle()
    turt.penup()
    turt.speed(0)
    turt.hideturtle()

    x = -WIDTH/2 + SPACING 
    cols = ["blue", "red", "yellow"]
    for count in range(num):
        turt.setx(x)
        turt.sety(ycoord)
        #print("t at",turt.xcor(),turt.ycor())
        turt.color(cols[count % len(cols)])
        SimpleTurtleShapes.drawOneSnowy(turt,size)
        x = x + size + SPACING
        
if __name__ == '__main__':
   
    # set up global state, WIDTH and HEIGHT
    # accessible as screen-size dimensions
    win = turtle.Screen()
    win.colormode(255)
    WIDTH = win.window_width()
    HEIGHT = win.window_height()
    
    # get number of drawables and create    
    size = 100
    num = WIDTH//(size + SPACING)   
    drawMany(num,size,0)
    
    size = 50
    num = WIDTH//(size + SPACING)
    drawMany(num,size,-size + SPACING)
    win.exitonclick()
