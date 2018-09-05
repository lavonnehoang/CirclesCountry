'''
Created on Mar 22, 2018

@author: lavonnehoang
'''
import random
import operator
DEBUG = False
def readWords(fname):
    """
    return a list of all strings
    stored in file whose path is fname
    format of file: one string per line
    """
    f = open(fname)
    data = []
    for line in f:
        data.append(line.strip())
    f.close()
    return data

def randWord(wordList):
    """
    returns a random word string chosen from the parameter 
    wordList, which is a list of words obtained from
    the readWords function where each element is a different
    word in the file
    """
    randomWord = random.randint(0,len(wordList))
    secret = wordList[randomWord]
    return secret

def update(letter,template, secretword):
    """
    called in the play function and takes the parameter of the letter
    which should be a character, a template which is a list, and a secretword which
    which is a string. returns a list which is altered each time the guessed letter 
    is in the program's secret word
    """
    pos = [x for x in range(len(secretword)) if secretword[x]==letter]
    for y in pos:
        template[y]=letter
    return template        

def createTemplate(current,word,letter):
    """
    takes three string parameters and called in the getNewWordList function.
    it creates a new template based on each new word and returns a string
    """
    newWord = list(current)
    for i in range(len(word)):
        if word[i] == letter:
            newWord[i] = letter
    return "".join(newWord) 

def getNewWordList(current,letter,wordList):    
    """
    current and letter are both string parameters and wordList is 
    a list parameter. called in the play function for each new guess.
    returns a two-tuple where the first element is 
    the template (a string) and the second element is
    an updated list of words that has the maximum  number of words.
    """
    templates = {}
    for word in wordList:
        currentW = createTemplate(current,word,letter)
#         if DEBUG:
#             print(word,currentW, current)
        if currentW not in templates:
            templates[currentW] = [word]
        else:
            templates[currentW].append(word)
    
    if DEBUG == True:
        toSort = []
        for item in templates:  
            toSort.append(["".join(item),len(templates[item])])            
        sortedTemplates = sorted(toSort, key = operator.itemgetter(1))    
        for item in sortedTemplates:
            print(item[0] + " " + str(item[1]))
        print("# keys = " + str(len(templates)))    
    maximum = 0 
    newList = []
    wordKey = ""
    for i in templates: 
        if len(templates[i]) > maximum:
            maximum = len(templates[i])
            newList = templates[i]
            wordKey = i
        if len(templates[i]) == maximum:
            if letter not in i:
                maximum = len(templates[i])
                newList = templates[i]
                wordKey = i
    return (wordKey,newList)           
        
def play():
    """
    simulates a game of hangman where the user must guess a word 
    that the computer generates. based on
    user input, the user is allowed a certain number of guesses for 
    each letter. when the user correctly guesses the word or the 
    number of misses is exceeded, the game ends. for each user guess,
    the computer changes the secret word to be a word from a list with 
    the most amount of valid words that match the user's previous inputs.
    the debug function allows the user to see the changing secret word 
    and the templates that the computer is choosing from
    """
    global DEBUG 
    
    words = readWords("data/lowerwords.txt")
    allowed = 0
    guesses = 0 
    deb = input("(d)ebug or (p)lay mode: ")
    if deb == "d":
        DEBUG = True
         
    
    print ("you'll get 12 misses unless you enter 'h' for 'hard to guess'")
    diff = input("(h)ard or (e)asy >")
    if diff == "h":
        print("you have 8 misses to guess word")
        allowed = 8
    if diff == "e": 
        print("you have 12 misses to guess word")
        allowed = 12
    wordLen = int(input("How many letters in the word you'll guess: "))
    
    guessedList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    valWords = []
    for i in words:
        if len(i)==wordLen:
            valWords.append(i)
    randomNum = random.randint(0,len(valWords))
    word = valWords[randomNum]
    
    misses = 0  
    updatedList = valWords 
    guessedWord = "_" * wordLen
    
    
    while True:
        print("letters not yet guessed:" + "".join(guessedList))
        print("misses remaining = " + str(allowed))
        print("secret so far: " + " ".join(guessedWord))
        if DEBUG:
            print ("(word is " + word + ")")
            print ("# possible words:" + str(len(updatedList))) 
        ucount = guessedWord.count("_")
        
        if ucount == 0: 
            
            print("you guessed the word: " + word)
            print("you made " + str(guesses) + " guesses with " + str(misses) + " misses")
            print(guessedWord)
            break
        
        letter = input("guess a letter: ")
        
        newTuple = getNewWordList(guessedWord, letter, updatedList)
        updatedList = newTuple[1]
        guessedWord = newTuple[0]
        word = randWord(updatedList) 
        
        if letter in word: 
              
            guessedList[guessedList.index(letter)] = " "
            guesses += 1 
            guessedWord= update(letter, list(guessedWord), word)
            print("you guessed " + letter + " correctly!")
                
        else:
            if letter not in guessedList:
                print("you already guessed that") 
            else:
                allowed -= 1
                guesses += 1
                misses += 1
                guessedList[guessedList.index(letter)] = " "
                print(letter + " is not in secret word")
        
        if allowed == 0:
            print("you lost!")
            print("word is " + word)
            print("you made " + str(guesses) + " guesses with " + str(misses) + " misses")
            break
            
    
        
if __name__ == '__main__':
    play()
    