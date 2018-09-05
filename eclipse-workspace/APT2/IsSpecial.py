'''
Created on Feb 8, 2018

@author: lavonnehoang
'''
def contains(thing, element):
    return element in thing
def lovely(ingredients,inedible):
    listIngredients = ingredients.split()
    xx = inedible.split()
    count = 0
    for one in listIngredients:
        if one not in xx:
            count = count + 1 
    return count
if __name__ == '__main__':
    x = "rice milk"
    y = "rice milk honey"
    print (lovely(x,y))