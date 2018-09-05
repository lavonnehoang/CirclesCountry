'''
Version 1.0: April 16, 2018

@author: ola
'''

import csv, operator

def get_header(fname):
    """
    fname is name of csv file with data
    and a header row
    returns a list of the labels in the header row
    """
    
    csvf = open(fname, 'r')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')

    header =  next(freader)
    return header

def most_cancelled(fname,size):
    """
    fname is name of CSV file with airport data
    size is # entries to return
    return list of tuples (TAC, # cancelled flights)
    where tup[0] is the three letter airport code 
    and tup[1] is an integer which is the number of
    cancelled flights at that airport
    
    return sorted high to low by tup[1], i.e., most cancelled
    flights first. Return only size entries
    """
    
    csvf = open(fname, 'r')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')

    header =  next(freader)
    print("header row labels",header)
    aird = {}
    for row in freader:
        airport = row[0]
        cancelled = int(row[3])

        if airport not in aird:
            aird[airport] = 0
        
        if cancelled >= 100:
            aird[airport] += 1
            
    data = sorted(aird.items())
    cancels = sorted(data,key=operator.itemgetter(1),reverse=True)

    return cancels[:size]

def busiest(fname,entries):
    csvf = open(fname, 'r')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    header =  next(freader)
    aird = {}
    
    for row in freader:
        airport = row[0]
        total = int(row[6])
            
        if airport not in aird:
            aird[airport] = [0,0]
        aird[airport][0] += total 
        aird[airport][1] += 1
    
        
    for item in aird:
        aird[item] = (aird[item][0])/(aird[item][1])
        
    data = sorted(aird.items())
    avgs = sorted(data,key=operator.itemgetter(1),reverse=True)
    return avgs[:entries]

def ontime(fname, entries):
    csvf = open(fname, 'r')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    header =  next(freader)
    aird = {}
    
    for row in freader:
        airport = row[0]
        total = int(row[6])
        ontime = int(row[7])
            
        if airport not in aird:
            aird[airport] = [0,0]
        aird[airport][0] += ontime 
        aird[airport][1] += total
    
        
    for item in aird:
        aird[item] = round((aird[item][0])/(aird[item][1])*100)
        
    data = sorted(aird.items())
    pctgs = sorted(data,key=operator.itemgetter(1),reverse=True)
    return pctgs[:entries]

if __name__ == '__main__':
    results = most_cancelled("data/airdata.csv",10)
    print(results)
    print(busiest("data/airdata.csv",3))
    print(ontime("data/airdata.csv",6))
