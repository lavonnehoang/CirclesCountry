'''
Created on Mar 22, 2018

@author: lavonnehoang
'''
import random

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
    randomNum = random.randint(5,10)
    valWords = []
    for i in wordList:
        if len(i)==randomNum:
            valWords.append(i)
    print(valWords)
    randomWord = random.randint(0,len(valWords))
    secret = valWords[randomWord]
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

def play():
    """
    simulates a game of hangman where the user must guess a word 
    that the computer generates from the randomWord function. based on
    user input, the user is allowed a certain number of guesses for 
    each letter. when the user correctly guesses the word or the 
    number of misses is exceeded, the game ends
    """
    words = readWords("data/lowerwords.txt")
    allowed = 0
    guesses = 0 
    print ("you'll get 12 misses unless you enter 'h' for 'hard to guess'")
    diff = input("(h)ard or (e)asy >")
    if diff == "h":
        print("you have 8 misses to guess word")
        allowed = 8
    if diff == "e": 
        print("you have 12 misses to guess word")
        allowed = 12
    
    guessedList = []
    
    misses = allowed   
    word = randWord(words)
    guessedWord = ["_" for i in range(len(word))]
    
    while True:
        print("letters you've guessed:" + " ".join(sorted(guessedList)))
        print("misses remaining = " + str(misses))
        print(" ".join(guessedWord))
        ucount = guessedWord.count("_")
        
        
        if ucount == 0: 
            print("you guessed the word: " + word)
            print("you made " + str(guesses) + " guesses with " + str(misses) + " misses")
            break
        letter = input("letter> ")
        
        
        if letter in word:
            if letter not in guessedList:               
                guessedList.append(letter)
                guesses += 1 
                guessedWord= update(letter, guessedWord, word)
                
        else: 
            if letter in guessedList:
                print("you already guessed that")
            else:
                misses -= 1
                guesses += 1
                guessedList.append(letter)
                print("you missed: " + letter + " not in word")
        
        if misses == 0:
            print("you're hung!!!")
            print("word is " + word)
            print("you made " + str(guesses) + " guesses with " + str(misses) + " misses")
            break
            
    
        
if __name__ == '__main__':
    play()
    