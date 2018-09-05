'''
Created on Apr 11, 2018

@author: ola
'''
import math
def averages(items,ratings):
    d = {}
    for name in items:
        if name not in d:
            d[name] = [0,0]
        for i in ratings.values():
            if math.fabs(i[items.index(name)]) > 0:
                d[name][1] += 1
                d[name][0] += float(i[items.index(name)])
    for item in d:
        if d[item][1] == 0:
            d[item] = 0
        if d[item] != 0:
            d[item] = (d[item][0])/(d[item][1])
    data = sorted(d.items())
    avgs = sorted(data, key = lambda x: x[1], reverse = True)
    return avgs
        
def similarities(name,ratings):
    d = {}
    ans = {}
    for item in ratings:
        if item not in d:
            d[item] = [ratings[name][i]*ratings[item][i] for i in range(len(ratings[name])) if item != name]
    for i in d:
        if d[i] != []:
            ans[i] = sum(d[i]) 
    data = sorted(ans.items())
    listAns = sorted(data, key = lambda x: x[1], reverse = True)
    return listAns
        
 
def recommendations(name,items,ratings,size):
    simil = similarities(name,ratings)[:size]

    weightedA = {}
    for x in simil:
        person = x[0]
        score= x[1]
        weightedA[person] = [(score)*(ratings[person][i]) for i in range(len(ratings[person]))]
    d = {}
    for restaurant in items:
        if restaurant not in d:
            d[restaurant] = [0,0]
        for i in weightedA.values():
            if math.fabs(i[items.index(restaurant)]) > 0:
                d[restaurant][1] += 1
                d[restaurant][0] += float(i[items.index(restaurant)])

    for item in d:
        if d[item][1] == 0:
            d[item] = 0
        if d[item] != 0:
            d[item] = (float(d[item][0]))/(float(d[item][1]))
    data = sorted(d.items())
    avgs = sorted(data, key = lambda x: x[1], reverse = True)
    return avgs
    
        

if __name__ == '__main__':
    items = ["DivinityCafe", "FarmStead", "IlForno",
     "LoopPizzaGrill", "McDonalds", "PandaExpress",
     "Tandoor", "TheCommons", "TheSkillet"]
    
    ratings = {"Sarah Lee":
   [3, 3, 3, 3, 0, -3, 5, 0, -3],
 "Melanie":
   [5, 0, 3, 0, 1, 3, 3, 3, 1],
  "J J":
   [0, 1, 0, -1, 1, 1, 3, 0, 1],
  "Sly one":
   [5, 0, 1, 3, 0, 0, 3, 3, 3],
  "Sung-Hoon":
   [0, -1, -1, 5, 1, 3, -3, 1, -3],
  "Nana Grace":
   [5, 0, 3, -5, -1, 0, 1, 3, 0],
  "Harry":
   [5, 3, 0, -1, -3, -5, 0, 5, 1],
  "Wei":
   [1, 1, 0, 3, -1, 0, 5, 3, 0]
}
    
    print(averages(items,ratings))
    print(similarities("Sarah Lee", ratings)) 
    print(recommendations("Sarah Lee", items, ratings, 3))

