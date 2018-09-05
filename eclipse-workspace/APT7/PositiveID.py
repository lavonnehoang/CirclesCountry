'''
Created on Apr 19, 2018

@author: lavonnehoang
'''

def maximumFacts(suspects):
    d = []
    best = 0
    for suspect in suspects:
        x = suspect.split(",") 
        d.append(x)
    
    for x in range(len(d)):
        for y in range(x+1,len(d)):
            same = list(set(d[x]) & set(d[y]))
            if len(same) > best:
                best = len(same)
    return best


if __name__ == '__main__':
    data = ["blond,tall,skinny","short,skinny,blond,tattooed","scarred,bald"]
    print(maximumFacts(data))
