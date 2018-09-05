'''
Created on Mar 21, 2018

@author: lavonnehoang
'''

def count(a,b):
    common = 0
    listA = list(a)
    listB = list(b)
    for charA in listA:
        if charA in listB: 
            common += 1
            i = listB.index(charA)
            del listB[i]
                
    return common             
    
if __name__ == '__main__':
    w2 = "horse"
    w1 = "seems"
    print(count(w1,w2))