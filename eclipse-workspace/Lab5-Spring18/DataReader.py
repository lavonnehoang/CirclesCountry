'''
Created on Feb 25, 2018

@author: ola
'''
import csv, math


def readit(fname):
    temp = open(fname, encoding="utf-8")
    f = csv.reader(temp, delimiter=',', quotechar='"')
    header = next(f)
    data = []
    for line in f:
        geo = line[-1].split(";")
        if(len(geo) > 1):
            geo[0] = float(geo[0])
            geo[1] = float(geo[1])
            line[-1] = geo
            data.append(line)
    return data

def haversine(lat1, lon1, lat2, lon2):
 
    R = 3959  # Earth radius in miles
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
 
    a = math.sin(dLat / 2) ** 2 + \
         math.cos(lat1) * math.cos(lat2) * math.sin(dLon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
 
    return R * c


def nearby(data,lat,long,threshold=25):
    global dukelat,dukelong
    for rest in data:
        if rest[-2] != "FOOD":
            continue

        dist = haversine(lat,long,rest[-1][0],rest[-1][1])
        if dist < threshold:
            print(rest[1],dist)

if __name__ == "__main__":
    dukelat = 36.0015321
    dukelong = -78.9400087
    data = readit("data/restaurants-data.csv")
    nearby(data,dukelat,dukelong,0.5)
