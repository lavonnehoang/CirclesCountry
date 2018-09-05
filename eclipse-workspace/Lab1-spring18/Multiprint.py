'''
Created on Jan 21, 2018

@author: ola
'''
word = "wonderful"
count = 1

def countprint():
    global count,word
    print(count,"\t",word)
    count = count + 1
    
def f1():
    countprint()
    countprint()

def f2():
    f1()
    f1()

def verse(callme):
    callme()
    callme()

if __name__ == '__main__':
    verse(f2)