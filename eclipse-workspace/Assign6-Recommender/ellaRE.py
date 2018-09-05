'''
Created on Apr 23, 2018

@author: lavonnehoang
'''
'''
Created on Apr 11, 2018

@author: ola
'''
import operator
import MovieReader
def averages(items,ratings):
    """
    this goes through the ratings and creates
    an average for each item based only on non-zero ratings.
    the returned list of tuples gives the items and their corresponding
    average score.  this list is in order of highest average to lowest
    with ties broken by alphabetized item names
    """
    d={}
    for k in items:
        location=items.index(k)
        for i in ratings:
            if k not in d:
                d[k]=[]
            if ratings[i][location]!=0:
                d[k].append(ratings[i][location])
        d[k]=(sum(d[k]))/float(len(d[k]))
    y=sorted(d.items())
    z=sorted(y, key=operator.itemgetter(1),reverse=True)
    return z


def similarities(name,ratings):
    """
    this returns a list of tuples of names of other users
    and their corresponding similarity score to the name in the
    parameter.  this score is created by taking the dot product between
    each users score and the parameterized user.
    this list is then sorted from highest similarity score to lowest
    with ties broke by alphabetical order
    """
    list1=ratings[name]
    d={}
    for k in ratings.keys():
        if k!=name:
            if k not in d:
                d[k]=[]
            for i in range(len(list1)):
                p=list1[i]*ratings[k][i]
                d[k].append(p)
            
    for l in d.keys():
        d[l]=sum(d[l])
    y=sorted(d.items())
    z=sorted(y, key=operator.itemgetter(1),reverse=True)
    return z
 
def recommendations(name,items,ratings,size):
    """
    this returns a list of tuples of items and their
    corresponding weighted average which is calculated by multiplying
    users ratings by their similarity score to the user in the parameter
    and then adding up these weighted scores and dividing by the number 
    of non-zero ratings.this list is then sorted from highest weighted average to lowest
    with ties broke by alphabetical order
    """
    l=similarities(name, ratings)
    l=l[:size]
    l=dict(l)
    d={}
    c={}
    
    for m in ratings.keys():
        list2=[]
        if m in l.keys():
            score=l[m]
            for p in ratings[m]:
                rate=score*p
                list2.append(rate)
            d[m]=list2
    for places in items:
        dex=items.index(places)
        c[places]=[]
        for people in d.values():
            c[places].append(people[dex])
    for q in c.keys():
        count=0
        for e in c[q]:
            if e!=0:
                count+=1
        if count!=0:
            c[q]=sum(c[q])/count
        if count==0:
            c[q]=0
    y=sorted(c.items())
    z=sorted(y, key=operator.itemgetter(1),reverse=True)
    return z

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
