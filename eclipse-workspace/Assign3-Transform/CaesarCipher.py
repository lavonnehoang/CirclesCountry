'''
Created on Mar 6, 2018

@author: lavonnehoang
'''
"""
given shift values
"""
shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def setShift(x):
    """
    changes the shift which alters the coded
    upper and lower case alphabets with the parameter x, 
    an integer
    """
    global shift, shifted_lower, shifted_upper
    shift = x
    shifted_lower = lower_alph[x:] + lower_alph[:x]
    shifted_upper = upper_alph[x:] + lower_alph[:x]
    
def findShift(string):
    """
    creates a set from the file of words in
    lowerwords.txt and then loops through the string
    parameter 26 times to give all possible Caesar
    cipher encryptions and finds the encryption that 
    has the most intersections with the set of available 
    words; subtracts this encrpytion with 26 to find the 
    original shift used; parameter string is an encrypted string
    """ 
    setWords = set()
    values = 0
    file = open("data/lowerwords.txt","r")
    for line in file:
        setWords.add(line.strip())
    for sh in range(26):
        setShift(sh)
        encrypted = (encrypt(string)).split()
        setEncrypted = set(encrypted)
        intersection = len(setWords & setEncrypted)
        if intersection > values:
            values = intersection
            x = sh
    return 26 - x

def encrypt(word):
    """
    creates an encrypted string from the parameter
    word, a string, by looping over the given string 
    and matching it with a letter in the encrypted
    alphabet defined as a global variable
    """
    encrypted = ''
    for ch in word:
        if ch in lower_alph:
            a = lower_alph.index(ch)
            encrypted += shifted_lower[a]
        elif ch in upper_alph:
            b = upper_alph.index(ch)
            encrypted += shifted_upper[b]
        else:
            encrypted += ch
    return encrypted
            

if __name__ == '__main__':
    setShift(10)
    ew = encrypt("zebra")
    setShift(16)
    w = encrypt(ew)
    print(ew,w)
    f = open("data/twain-csr.txt")
    st = f.read()
    shift = findShift(st)
    print(shift)

