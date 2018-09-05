'''
Created on Mar 21, 2018

@author: lavonnehoang
'''

def whosDishonest(club1, club2, club3):
    set1 = set(club1)
    set2 = set(club2)
    set3 = set(club3)
    common1 = set1 & set2
    common2 = set2 & set3
    common3 = set1 & set3
    s = set()
    s.update(common1)
    s.update(common2)
    s.update(common3)
    cheat = list(s)
    cheat = sorted(cheat)
    return cheat

if __name__ == '__main__':
    l1 = ["DOUG","DOUG","DOUG","DOUG","DOUG"]
    l2 = ["BOBBY","BOBBY"]
    l3 = ["JAMES"]
    print(whosDishonest(l1,l2,l3))