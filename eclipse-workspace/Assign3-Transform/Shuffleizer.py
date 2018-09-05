'''
Created on Mar 1, 2018

@author: lavonnehoang
'''
import random
def encrypt(word):
    
    if len(word) <= 2:
        return word
    
    rest = word[1:-1]
    lrest = list(rest)
    random.shuffle(lrest)
    rest = ''.join(lrest)
    
    return word[0] + rest + word[-1]

if __name__ == '__main__':
    words = ["hello", "goodbye", "enthralling", "I", "am"]
    for w in words:
        print(w,encrypt(w))