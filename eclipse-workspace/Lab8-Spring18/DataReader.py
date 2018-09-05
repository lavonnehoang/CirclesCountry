'''
Version 3 on March 26, 2018
Version 2 on November 1, 2015
Original: Oct 24, 2012

@author: ola
'''

import csv

def readandprocess(name):
    csvf = open(name, 'r')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datad = {}
    
    header =  next(freader)
    print("header row labels",header)
    for row in freader:
        #print row
        artist = row[2]
        song = row[1]
        if artist not in datad: 
            datad[artist] = [song]
        else:
            datad[artist].append(song)
     
    letters = {}        
    for artist in datad:
        songs = datad[artist]
        for song in songs:
            name = song.split()
            for word in name:
                count = len(word)
                if count >3:
                    if word not in letters:
                        letters[word] = 1 
                    else:
                        letters[word] += 1

    
    info = datad.items() 
    tosort = [(len(t[1]),t[0]) for t in info] 
    info = sorted(tosort) 
    print(info[-30:])
    
    info1 = letters.items()
    tosort1= [(x[1],x[0]) for x in info1]
    info1 = sorted(tosort1)
    print(info1[-5:])

    
        


if __name__ == '__main__':
    readandprocess("data/top1000.csv")
