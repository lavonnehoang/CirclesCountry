'''
Created on Jan 21, 2018

@author: ola
'''

def line(count):
    """
    print a design
    """
    stars = (2*count)-1    
    y = " " * (20-count)
    x = "*" * stars
    print(y+x)

    

if __name__ == '__main__':
    low = 1
    high = 11
    for x in range(low,high):
        line(x)