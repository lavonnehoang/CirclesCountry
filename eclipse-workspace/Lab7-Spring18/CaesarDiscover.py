'''
Created on Mar 21, 2018

@author: lavonnehoang
'''
import SimpleCaesar
def read():
    file = open("data/lowerwords.txt","r")
    listWords = []
    for line in file:
        listWords.append(line.strip())
    setWords = set(listWords)
    return setWords

def getMatches(collection):
    list = []
    for i in range(1,26): 
        for word in collection:
            encrypted = SimpleCaesar.encrypt(word,i)
            if encrypted in collection: 
                list.append([i,word,encrypted])
    for item in list:
        print(str(item[0]) + " " + item[1] + " " + item[2])
    print(len(list))
                
                
            
             
                
            
            
    
if __name__ == '__main__':
    collection = read()
    getMatches(collection)