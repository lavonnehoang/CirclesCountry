'''
Created on Feb 5, 2018

@author: ola
'''
def getList(data, year):
    year_list = []
    for one in data:
        if one[2] == year:
            year_list = year_list + [one]
    return year_list

def findAverage(data):
     total = 0 
     for lst in data:
          total = total + lst[1]
     return total/len(data)

def file2list(fname):
    f = open(fname)
    allData = []
    for line in f:
        line = line.strip()
        data = line.split(";")
        data[1] = int(data[1])
        data[2] = int(data[2])
        
        allData.append(data)
        
    f.close()
    return allData

def processFile(fname):
    data = file2list(fname)
    for one in data:
        print(one)
    print (getList(data, 1997))
    print (len(getList(data,1996)))
    print(findAverage(data))


if __name__ == '__main__':
    processFile("grades.txt")
    
