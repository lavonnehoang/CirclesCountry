'''
Created on Feb 6, 2018

@author: lavonnehoang
'''

def label(size):
    if size <= 3:
        return "cancelled"
    elif 4 <= size <= 18:
        return "seminar"
    elif 19 <= size <= 44:
        return "medium"
    elif 45 <= size <= 199:
        return "large"
    elif size >= 200:
        return "enormous"

if __name__ == '__main__':
    print (label(3))