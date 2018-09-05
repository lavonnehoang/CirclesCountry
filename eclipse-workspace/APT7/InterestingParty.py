'''
Created on Apr 19, 2018

@author: lavonnehoang
'''

def bestInvitation(first,second):
    d = {}
    for i in first:
        if i not in d: 
            d[i] = 0
        if i in d:
            d[i] += 1
    for i in second:
        if i not in d: 
            d[i] = 0
        if i in d:
            d[i] += 1
            
    sortedList = sorted(d.items(), key = lambda x: x[1], reverse = True)
    
    return sortedList[0][1]


if __name__ == '__main__':
    first =  ["fishing", "gardening", "swimming", "fishing"]
    second = ["hunting", "fishing", "fishing", "biting"]
    
    print(bestInvitation(first, second))