'''
Created on Mar 29, 2018

@author: lavonnehoang
'''

def freqs(data):
    elt = []
    counts = []
    for word in data:
        if word not in elt:
            elt.append(word)
    elt = sorted(elt)
    for x in elt:
        counts.append(data.count(x))
    return counts

if __name__ == '__main__':
    data = ["apple", "pear", "cherry", "apple", "cherry", "pear", "apple", "banana"]
    print(freqs(data))