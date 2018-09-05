'''
Created on Apr 23, 2018

@author: lavonnehoang
'''
import csv

def getData():
    csvf = open("data/movies.txt")
    f =csvf.readlines()
    movies = set()
    d = {}
    
    for row in f:
        row = row.strip().split(",")
        movie = row[1]
        movies.add(movie)       
        student = row[0]
        rating = float(row[2])
        if student not in d:
            d[student] = []
        d[student].append(tuple((movie, rating)))
        
    movies = sorted(list(movies))

    for person in d.keys():
        d[person] = sorted(d[person])
        for movie in movies:
            dex = movies.index(movie)
            if len(d[person])< dex + 1:
                d[person].append(tuple((movie,0)))
                d[person] = sorted(d[person])
            if d[person][dex][0] != movie:
                d[person].append(tuple((movie,0)))
                d[person] = sorted(d[person])
        
        
        rates = []   
        x = sorted(d[person])
        d[person] = x
        for tup in d[person]:
            rates.append(tup[1])
        d[person] = rates
        
        
        return (tuple((movies,d)))
            
    

if __name__ == '__main__':
    print(getData())