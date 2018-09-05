'''
Created on Mar 8, 2018

@author: lavonnehoang
'''

import random

def commonCount(a,b):
    if a == "ghost":
        return 2
    return 3

def playGame():
    f = open("kwords5.txt")
    words = f.read().split()
    print("read", len(words),"words")
    rword = random.choice(words)
    print ("I guess", rword)
    common = input("letters in common ")
    common = int(common)
    print("# in common is", common)
    
    newWords = []
    for w in words:
        com = commonCount(rword,b)
        if com == common:
            newWords.append(w)
        
    words = newWords
    print("number of words is", len(words))

if __name__ == '__main__':
    pass