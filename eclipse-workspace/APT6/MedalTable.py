'''
Created on Mar 27, 2018

@author: lavonnehoang
'''
import operator
def generate(results):
    d = {}
    for x in results:
        data = x.split()
        gold = data[0]
        silver = data[1]
        bronze = data[2]
        
        if gold not in d:
            d[gold] = [0,0,0]
        if silver not in d:
            d[silver] = [0,0,0]
        if bronze not in d:
            d[bronze] = [0,0,0]
            
        d[gold][0] += 1
        d[silver][1] += 1
        d[bronze][2] += 1
    
    w = sorted(d.items()) 
    yy = [(x[0],x[1][0], x[1][1], x[1][2]) for x in w]   
    x = sorted(yy, key=operator.itemgetter(3), reverse = True)
    y = sorted(x, key=operator.itemgetter(2), reverse = True) 
    z = sorted(y, key=operator.itemgetter(1), reverse = True)  
    return [a[0] + " " + str(a[1]) + " " + str(a[2]) + " " + str(a[3]) for a in z]
    
if __name__ == '__main__':
    results = ["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"]
    print(generate(results))
