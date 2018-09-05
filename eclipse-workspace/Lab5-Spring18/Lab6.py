'''
Created on Mar 8, 2018

@author: lavonnehoang
'''
import math

def distance(a, b): 
    """ 
    Parameters a and b are both 2-tuples
    calculate and return distance between 
    points a and b
    """ 
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def minDistance(points):
    vals = []
    for j in range(len(points)):
        for i in range (j+1,len(points)):
            vals.append(distance(points[j], points[i]))
    return min(vals)
        
    


if __name__ == '__main__':
    points = [(-7, 2), (-6, 6), (1, 2), (4, 5), (9, -6)]
    print(minDistance(points))
