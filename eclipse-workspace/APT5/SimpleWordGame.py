'''
Created on Mar 20, 2018

@author: lavonnehoang
'''

def points(player,dictionary):
    recall = set()
    score = 0
    for word in player: 
        if word in dictionary and word not in recall: 
            recall.add(word)
            score += len(word)**2
    return score

if __name__ == '__main__':
    p=["apple", "orange", "strawberry" ]

    d=[ "strawberry", "orange", "grapefruit", "watermelon" ]
    
    print(points(p,d))