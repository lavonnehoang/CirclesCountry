'''
Created on Mar 29, 2018

@author: lavonnehoang
'''
def countVisible(trophies):
    visible = [0,0]
    initr = 0
    initl = 0 
    right = 0
    left = 0
    reversedShelf = trophies[::-1]
    for height in trophies:
        if height > initr:
            initr = height
            right += 1
    visible[0] = right
    for height in reversedShelf:
        if height > initl:
            initl = height
            left += 1
    visible[1] = left
    return visible
            
        
            
if __name__ == '__main__':
    trophies = [1,2,3,4,5]
    print(countVisible(trophies))
