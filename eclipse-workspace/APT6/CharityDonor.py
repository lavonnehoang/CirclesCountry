'''
Created on Mar 28, 2018

@author: lavonnehoang
'''
import operator
def nameDonor(contributions):
    d = {}
    for i in contributions:
        data = i.split(":")
        name = data[0]
        amount = float(data[1])
        if name not in d:
            d[name] = 0
        d[name] += amount
        
    x = sorted(d.items())
    y = [(a[0],a[1]) for a in x]
    z = sorted(y, key=operator.itemgetter(1),reverse = True)
    return z[0][0]


if __name__ == '__main__':
    names = ["Zack:800.00", "Gregory:900.00"] 
    print(nameDonor(names))