'''
Created on Sep 20, 2015

@author: ola
'''
import random
import turtle


def gcolor(val):
    """
    return a shade of gray
    """
    x = 255 - 5*val
    if x < 0:
        x = 0
    return (x,x,x)

def walk(turt,n,visualize,ycoord):
    """
    Use turt (a turtle) to simulate a random
    walk of n-steps where n is an int
    If visualize is True then use turtle to visualize,
    otherwise just simulate and return result
    ycoord is used for visualization so they can be "stacked"
    
    returns a list of how many times each location visited
    where list[0] represents location -n, list[-1] represents n
    """
    current = 0
    visits = [0]*(2*n+1)
    
    if visualize:
        turt.penup()
        turt.color(255,255,255)
        turt.goto(0,ycoord)
        
    while visits[0] == 0 or visits[-1] == 0:
        flip = random.randrange(0,2);
        if flip == 0:
            current += 1
        else:
            current -= 1
        if current > n:
            current = n
        if current < -n:
            current = -n
        visits[current+n] += 1
        if visualize:
            turt.stamp()
            vc = visits[current+n]
            turt.goto(size*current,ycoord)
            turt.color(gcolor(vc))
    return visits

def simulate(size,trials,turt):
    total = 0
    ystart = 0
    for _ in range(trials):
        results = walk(turt, size,False,ystart)
        print(sum(results),results)
        total += sum(results)
        ystart += 25
    print("average for %d walks of size %d: %1.3f\n" % (trials,size,total/trials))


if __name__ == "__main__":
    turt = turtle.Turtle()
    turt.speed(0)
    wn = turtle.Screen()
    wn.colormode(255)
    random.seed(1234)
    turt.shape("square")
    size = int(input("#steps to visualize in one walk "))
    trials = int(input("#number of simulations "))
    simulate(size,trials,turt)
    
    wn.exitonclick()