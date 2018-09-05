'''
Created on Mar 6, 2018

@author: lavonnehoang
'''

def indexFirstVowel(word):
    """
    returns the index of the first vowel in 
    a word if the word doesn't start with a 
    vowel or "qu"; treats y as a vowel in this case;
    parameter word is a string first passed through 
    the encrypt function
    """
    for i in range(len(word)):
        if word[i] in "aeiouyAEIOUY":
            return i 
    return -1 

def encrypt(w):
    """
    encrypts a string into Pig Latin with
    the given rules in the assignment by using
    if statements for conditions;
    parameter w is a string
    """
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if w[0] in vowels:
        return w + "-way"
    if w[0] == 'q':
        return w[2:] + "-quay" 
    if w[0] == 'y' or w[0] == 'Y':
        return w[1:] + "-" + w[0] + "ay"
    x = indexFirstVowel(w)
    if x == -1:
        return w + "-way"
    return w[x:] + "-" + w[:x] + "ay"

def decrypt(w):
    """
    decrypts a string using the rules given for 
    the encrypt function; may not return the same 
    original word because some encrypted words are 
    the same; parameter w is a string 
    """
    if "-way" in w:
        a = w.index("-way")
        return w[:a]
    if "-quay" in w:
        a = w.index("-quay")
        return "qu" + w[:a]
    begin = w.index("-")
    end = w.rindex("ay")
    return w[begin+1:end] + w[:begin]

    
if __name__ == '__main__':
    print(encrypt("yesterday"))
    print(decrypt("apple-way"))
    

    