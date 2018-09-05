'''
Created on Feb 27, 2018

@author: lavonnehoang
'''

def theIndex(carrots,amount):
    while amount>0:
        a = max(carrots)
        index = carrots.index(a)
        carrots.index(a) -= carrots.index(a)-1 
        amount -= 1

if __name__ == '__main__':
    pass