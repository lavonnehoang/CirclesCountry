'''
Created on Feb 20, 2018

@author: lavonnehoang
'''

def check(word):
    valid = ["pi", "ka", "chu"]
    while (len(word) > 0):
        wordok = False
        for w in valid:
            if word.startswith(w):
                word = word[len(w):]
                wordok = True
        
        if not wordok:
            return "NO"
    return "YES"

if __name__ == '__main__':
    print(check("pipipik"))