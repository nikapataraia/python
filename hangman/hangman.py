from operator import contains
from random import randint
from re import match
from traceback import print_list # Do not delete this line

def displayIntro():
    file = open("hangman-ascii.txt", "r")
    lines = list(range(0,23))
    for pos, line in enumerate(file):
        if pos in lines:
            print(line.rstrip())
        elif pos > 23 : break
    file.close()
    
    

def displayEnd(result):
    if(result):
        with open("hangman-ascii.txt") as file:
            lines = list(range(191,203))
            for pos, line in enumerate(file):
                if pos in lines:
                 print(line.rstrip())
                elif pos > 203 : break
    else:
        with open("hangman-ascii.txt") as file:
            lines = list(range(99,112))
            for pos, line in enumerate(file):
                if pos in lines:
                 print(line.rstrip())
                elif pos > 203 : break

        
         

    
            
def displayHangman(state):
    lines = list
    if(state == 1): lines = list(range(23,33))
    if(state == 2): lines = list(range(37,46))
    if(state == 3): lines = list(range(50,59))
    if(state == 4): lines = list(range(63,72))
    if(state == 5): lines = list(range(76,85))
    if(state == 6): lines = list(range(89,98))
    with open("hangman-ascii.txt") as file:
            for pos, line in enumerate(file):
                if pos in lines:
                 print(line.rstrip())


def getWord():
    with open("hangman-words.txt") as file:
        words = file.readlines()
        rand = randint(0,843)
        return words[rand].rstrip()

def valid(c):
    if(c == "" or len(c) > 1): return False
    index = ord(c)
    checker = list(range(97,123))
    return index in checker

def play():
    myword = str(getWord())
    guessingword = ""
    for x in range(len(myword)):
        guessingword += "_"
    letterlist = []
    for el in myword:
        if(not contains(letterlist,el)):
            letterlist.append(el)
    letterlist = list(dict.fromkeys(letterlist))
    x = 1
    while x<7:
        if(len(letterlist) == 0): 
            print("Hidden word was: " + myword)
            return True
        displayHangman(x)
        if(x == 6): break
        print("guess word: " + guessingword)
        print("Enter the letter: ")
        c = input()
        while(not valid(c)):
            print("Please Enter the letter again: ")
            c = input()
        if(contains(letterlist,c)):
            letterlist.remove(c)
            onindexes = []
            y = 0
            for el in myword:
                if(el == c):
                    onindexes.append(y)
                y = y+1
            for z in range(len(myword)):
                if z in onindexes:
                    guessingword = guessingword[:z] + c + guessingword[z+1:]
        else :
             x = x +1
    print("Hidden word was: " + myword)
    return False



        

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        answer = input("Do you want to play again? (yes/no)")
        if(answer == "no"):break
        while(answer != "yes"):answer = input("Do you want to play again? (please enter valid argument) (yes/no)")

if __name__ == "__main__":
    hangman()

