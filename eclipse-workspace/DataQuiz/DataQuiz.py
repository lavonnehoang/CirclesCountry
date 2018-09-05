'''
Created on Apr 20, 2018

@author: ola
'''
import csv 


def verify(fname):
    csvf = open(fname, 'r', encoding="utf-8")
    freader = csv.reader(csvf,delimiter=';',quotechar='"')

    header =  next(freader)  # skip header row
    count = 0
    for _ in freader:
        count += 1
    
    return count

def donors(fname, size, lowerbound):
       
        csvf = open(fname, 'r')
        freader = csv.reader(csvf, delimiter=';', quotechar='"')
        
        d = {}

        header = next(freader)
        for row in freader:
            name = row[11]
            amount = float(row[19])
            if name not in d:
                d[name] = 0
            if amount >= lowerbound:
                d[name] += 1
        data = sorted(d.items())
        ans = sorted(data, key = lambda x: x[1], reverse = True)
        final = ans[:size]
        return final 

def received(fname, size):
    csvf = open(fname, 'r')
    freader = csv.reader(csvf, delimiter=';', quotechar='"')
        
    d = {}

    header = next(freader)
    for row in freader:
        recipient = row[1]
        amount = float(row[19])
        if recipient not in d:
            d[recipient] = [0,0]
        d[recipient][0] += 1
        d[recipient][1] += amount
    data = [(k,v[1],v[1]/v[0]) for k,v in d.items()]

    avgs = sorted(data, key = lambda x: x[1], reverse = True)
    return avgs[:size]

if __name__ == '__main__':
    name = "data/durham-political.csv"
    count = verify(name)
    print("# of lines read = ",count)
    print(donors("data/durham-political.csv",10,0))
    print(received("data/durham-political.csv",8))
   
