'''
Created on Feb 8, 2018

@author: lavonnehoang
'''
def getscore(toss,roll):
    return roll*toss.count(roll)
def maxPoints(toss):
    best = 0
    for d in [1,2,3,4,5,6]:
        sc = getscore (toss,d)
        if sc > best:
            best = sc            
    return best
    
if __name__ == '__main__':
    
    print(maxPoints([1,2,3,4,5,6]))