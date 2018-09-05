'''
Created on Apr 7, 2018

@author: lavonnehoang
'''

def common(numbers):
    allNum = set()
    for item in numbers:
        item = item.split(" ")
        for elt in item:
            allNum.add(int(elt))
    l1 = list(allNum)
    l2 = sorted(l1)
    return l2


if __name__ == '__main__':
    numbers = ["1 2 3", "1 2 3", "1 2 3", "1 2 3"]
    print(common(numbers))