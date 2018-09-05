'''
Created on Mar 28, 2018

@author: lavonnehoang
'''

def findLabel(labels,deeds,needs):
    ds = set(deeds)
    for i in range(len(needs)):
        completed = needs[i].split()
        cs = set(completed)
        if cs <= ds:
            return labels[i]
    return "nobadge"
            
if __name__ == '__main__':
    labels = ['beginner', 'novice', 'intermediate', 'expert']
    deeds = ['skip', 'hop', 'wobble']
    needs = ['skip run walk talk', 'wobble teeter fall skip', 
         'skip hop', 'skip hop wobble']
    
    print(findLabel(labels,deeds,needs))