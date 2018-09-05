'''
Created on Mar 20, 2018

@author: lavonnehoang
'''

def score(listA,listB,listC):
    scoreA = 0
    scoreB = 0
    scoreC = 0
    for word in listA: 
        if word in listB and word in listC:
            scoreA += 1
            scoreB += 1
            scoreC += 1
            listA.remove(word)
            listB.remove(word)
            listC.remove(word)
        elif word in listB and word not in listC:
            scoreA += 2
            scoreB += 2
            listB.remove(word)
            listA.remove(word)
        elif word in listC and word not in listB:
            scoreA += 2
            scoreC += 2
            listC.remove(word)
            listA.remove(word)
        elif word not in listC and word not in listB:
            scoreA += 3
    for word in listB: 
        if word in listC and word not in listA:
            scoreB += 2
            scoreC += 2
            listC.remove(word)
        else:
            scoreB += 3
    for word in listC:
        scoreC += 3
    return str(scoreA) + "/" + str(scoreB) + "/" + str(scoreC)     

if __name__ == '__main__':
    listA = ["cat", "dog", "pig", "mouse"]
    listB = ["cat", "pig"]
    listC = ["dog", "cat"]
    
    print(score(listA,listB,listC))