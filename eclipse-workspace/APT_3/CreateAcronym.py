'''
Created on Feb 14, 2018

@author: lavonnehoang
'''

def acronym(phrase):
    phrase = phrase.split()
    x = ""
    for i in range(len(phrase)):
        x += phrase[i][0]
    return x 

if __name__ == '__main__':
    print (acronym("Self Contained Underwater Breathing Apparatus"))