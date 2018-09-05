'''
Created on Apr 18, 2018

@author: ola
'''
import csv 

SQFT_INDEX = 46
BED_INDEX = 57
OWNER_INDEX = 12

def sqft(fname,size):
    csvf = open(fname, 'r', encoding="utf-8")
    freader = csv.reader(csvf,delimiter=';',quotechar='"')

    d = {}
    header =  next(freader)
    
    for row in freader:
        beds = int(row[BED_INDEX])
        sqft = int(row[SQFT_INDEX])
        if beds not in d:
            d[beds] = []
        d[beds].append(sqft)
        
    data = sorted(sorted(d.items()), key=lambda x: len(x[1]), reverse=True)
    return data[:size]

def owners(fname,size):
    csvf = open(fname, 'r', encoding="utf-8")
    freader = csv.reader(csvf,delimiter=';',quotechar='"')

    d = {}
    header =  next(freader)
    for row in freader:
        name = row[OWNER_INDEX]
        if name not in d:
            d[name] = 0
        d[name] += 1

    data = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return data[:20]

def count_lines(fname):
    csvf = open(fname, 'r', encoding="utf-8")
    freader = csv.reader(csvf,delimiter=';',quotechar='"')

    header =  next(freader)
    print(list(enumerate(header)))
    
    lines = 0
    for _ in freader:
        lines += 1
    return lines

if __name__ == '__main__':
    source = "data/2017-real-property-list.csv"
    
    lines = count_lines(source)
    print("# of lines read = ",lines)
    data = owners(source,20)
    for each in data:
        print(each)
    
    data = sqft(source,20)
    for tup in data:
        print(tup[0],sum(tup[1])/len(tup[1]),len(tup[1]))
