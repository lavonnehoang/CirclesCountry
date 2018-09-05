'''
Created on Feb 18, 2018

@author: ola
'''
def hailstone(start,printing):
    """
    start is int value for hailstone/collatz
    return int: number of steps in sequence
    with 1 as last value of sequence, e.g.,
    starting at 1 is zero steps
    printing is boolean, if true print all values
    """
    
    steps = 0
    current = start
    while current != 1:
        if printing:
            print("%d\t%d" % (steps,current))
        if current % 2 == 0:
            current /= 2
        else:
            current = current * 3 + 1
        steps += 1
    
    if printing:
        print("%d\t%d" % (steps,current))
    return steps
        
def analyze(limit):
    counts = []
    for _ in range(limit+2):
        counts.append(0)
    
    for n in range(1,limit+1):
        counts[n] = hailstone(n,False)
        
    avg = sum(counts)/limit
    mx = max(counts)
    dex = counts.index(mx)
    print("average",avg)
    print("max is %d at %d" % (mx,dex))

if __name__ == '__main__':
#     s = hailstone(9,True)
#     print(s)
    analyze(10000)