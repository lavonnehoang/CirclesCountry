'''
Created on Feb 13, 2018

@author: lavonnehoang
'''

def indexFirstVowel(word):
    for i in range(len(word)):
        if word[i] in "aeiou":
            return i 
    return -1 

def convert(s):
    list = []
    vowels = ['a','e','i','o','u']
    if s[0] in vowels:
        return s + "-way"
    if s[0] == 'q':
        return s[2:] + "-quay"
    x = indexFirstVowel(s)
    return s[x:] + "-" + s [:x] + "ay"
            
            
    

if __name__ == '__main__':
    
    print (convert("small"))
    