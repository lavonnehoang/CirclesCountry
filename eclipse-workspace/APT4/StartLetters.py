'''
Created on Feb 20, 2018

@author: lavonnehoang
'''

def howManyLetters(phrase):
    phrase = phrase.lower()
    phraseSplit = phrase.split()
    count = 0
    init = []
    for i in phraseSplit:
        if i[0] not in init:
            count +=1
            init.append(i[0])
    return count
        
        

if __name__ == '__main__':
    print(howManyLetters("The cat in the hat comes back"))