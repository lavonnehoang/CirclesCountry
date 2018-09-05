'''
Created on Apr 7, 2018

@author: lavonnehoang
'''
import operator

def winners(ballot):
    people = {}
    sortedPeople = []
    winners = []
    numPeople = 0
    for item in ballot:
        item = item.split(" ")
        numPeople = len(item)
        for person in item:
            if person not in people:
                people[person] = 0
            people[person] += numPeople
            numPeople -= 1
    sortedPeople = sorted(people.items(), key=operator.itemgetter(1), reverse = True)
    for element in sortedPeople:
        if element[1] == sortedPeople[0][1]:
            winners.append(element[0])
    winners.append(sortedPeople[0][0])
    winners = set(winners) 
    winnersFinal = list(sorted(winners))
    return winnersFinal


if __name__ == '__main__':
    ballots = ["moe curly larry", "moe larry curly", "curly moe larry"]
    print(winners(ballots))
