'''
Created on Feb 13, 2018

@author: lavonnehoang
'''

def average(sentenceList):
    xx = []
    for i in sentenceList:
        xx += i.split()
    return len(xx)/len(sentenceList)
    
        

    

    
    

if __name__ == '__main__':
    print(average(["the cat ate","the dog"]))