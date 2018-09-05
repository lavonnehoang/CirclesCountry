\'''
Created on Jan 31, 2018

@author: ola
'''
import turtle,random, SimpleTurtleShapes


def drawMany():
    """
    Draw several "things" in a row
    """
    t1 = turtle.Turtle()
    t1.speed(0)
    width = turtle.Screen().window_width()
    radius = 60
    xcoord = -width/2 + radius

    for _ in range(8):
        t1.penup()
        t1.setx(xcoord)
        t1.sety(0)
        SimpleTurtleShapes.drawOneSnowy(t1,radius)
        xcoord = xcoord + 2*radius + 10

def drawManyRandom():
    """
    Draw several "things" in a row
    """
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.speed(0)
    width = turtle.Screen().window_width()
    height = turtle.Screen().window_height()
    radius = 60
    for _ in range(100):
        t1.penup()
        xc = random.randint(-width/2,width/2)
        yc = random.randint(-height/2,height/2-2*radius)
        t1.setx(xc)
        t1.sety(yc)
        SimpleTurtleShapes.drawOneSnowy(t1,radius)


if __name__ == '__main__':
    win = turtle.Screen()
    drawManyRandom()
    win.exitonclick()