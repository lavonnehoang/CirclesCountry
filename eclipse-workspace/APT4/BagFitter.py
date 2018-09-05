'''
Created on Feb 27, 2018

@author: lavonnehoang
'''

def bags(strength, food):
    bags = []
    counts = []
    for item in food:
        if item not in bags:
            bags.append(item)
            counts.append(0)
        location = bags.index(item)
        counts[location] += 1
    s = 0
    for x in counts:
        if x % strength == 0:
            s += x//strength
        else:
            s += (x//strength) +1 
    return s


    

if __name__ == '__main__':
    x = ["DAIRY", "DAIRY", "PRODUCE", "PRODUCE", "PRODUCE", "MEAT" ]
    print(bags(2,x))
