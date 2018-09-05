'''
Created on Mar 26, 2018

@author: ola
'''
import csv,sys

def readandprocess(name):
    csvf = open(name, encoding="utf-8")
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datad = {}
    header =  next(freader)
    print("header row labels",header)
    
    for row in freader:
        print(row)
       
  


if __name__ == '__main__':
    readandprocess("data/9600movies.csv")
