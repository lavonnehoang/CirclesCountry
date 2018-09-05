'''
Created on Feb 27, 2018

@author: lavonnehoang
'''


def howMany(meals, restaurant):
    names = []
    for each in meals:
        data = each.split(":")
        name = data[0]
        if data[1] == restaurant:
            if name not in names:
                names.append(name)        
    return len(names)

if __name__ == '__main__':
    meals = ["Sue:Elmos", "Joe:Mad Hatter", "Sue:Mad Hatter"]
    restaurant = "Elmos"
    print(howMany(meals,restaurant))