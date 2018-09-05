'''
Created on Feb 11, 2018

@author: lavonnehoang
'''
import turtle
wn = turtle.Screen()
lavonne = turtle.Turtle()

def drawOneHouse(turtle,size,baseColor, penColor):
    turtle.fillcolor(baseColor)
    turtle.pencolor(penColor)
    turtle.pensize(size)
    turtle.pendown()
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(size*5)
        turtle.right(90)
    turtle.end_fill()
    
    wn.exitonclick()

if __name__ == '__main__':

    drawOneHouse (lavonne, 20, "pink", "black")