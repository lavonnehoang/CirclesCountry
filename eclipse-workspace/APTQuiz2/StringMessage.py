'''
Created on Apr 7, 2018

@author: lavonnehoang
'''

def message(words, limit):
    finalWord = []
    accumulator = 0 
    for word in words:
        if accumulator <= limit:
            if accumulator < len(word):
                finalWord.append(word[accumulator%limit])
                accumulator += 1
            else: 
                accumulator+= 1
        if accumulator >= limit:
            accumulator = 0
            
    
    wordStr = "".join(finalWord)
    return wordStr

if __name__ == '__main__':
    words = ["happy", "dopey", "bashful", "sneezy"]
    limit = 10
    print(message(words,limit))