# Filename: hw7.py
# Author: Patrick Custer
# Section: 16
# Date: 11/3/2013
# Email: pcuste1@umbc.edu
# DEscription: Plays a hangman game

from random import randint

# Prints a greeting
# Input: none
# Output: none
def printGreeting():
    print("$ python hw7.py")
    print("-----------------------------------------------------------------")
    print("H A N G M A N")
    print("-----------------------------------------------------------------")
# reads the input file
# Input: File name
# Output: list of elements in the file
def readWords(filename): 
    inData = open(filename, "r")
    wordList = []
    for c in inData:
        wordList.append(c)
    return wordList

# Plays the game. 
# Input: list of words
# Output: 
def playGame(words): 
    while True:
        secretWord = getRandomWord(words).strip()
        print(secretWord)
        missedLetters = []
        correctLetters = []
        while (wonGame(correctLetters, secretWord) == False) and (lostGame(len(missedLetters)) == False):
            displayTurn(4 - len(missedLetters), correctLetters, secretWord)
            guess = getGuess(missedLetters + correctLetters)
            if guess.lower() in secretWord:
                print("Yes, there's a %s" %(guess))
                correctLetters.append(guess)
            else:
                print("No, there is not a %s" %(guess))
                missedLetters.append(guess)
        if (playAgain() == False):
            return

# Get a random word from the list of words
# Input: list of words
# Output: random word
def getRandomWord(words): 
    return words[randint(0,len(words))-1]

# Shows the display  for the entire game
# Input: Number of letters missed, correct letters and the secret word 
# Output: Text to the screen
def displayTurn(numMissedLetters, correctLetters, secretWord):
    wordSoFar = ""
    for c in secretWord:
        if c in correctLetters:
            wordSoFar += c
        else:
            wordSoFar += "_"
        wordSoFar += " "
    print ("%s %5sIncorrect guesses left: %s" %(wordSoFar,"",numMissedLetters))

# Gets a valid guessed letter from the user
# Input: list of guessed letters
# Output: Valid letter
def getGuess(allGuessedLetters):
    flag = True
    guess = ""
    while flag == True:
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("Only one letter please.")
        elif guess.lower() in allGuessedLetters:
            print("You already guessed", guess)
        elif (ord(guess.upper()) < 64) or (ord(guess.upper()) > 91):
            print("Only letters please.")
        else:
            flag = False
    return guess

# Determines whether or not the users has won the game
# Input: Correct letters and the secret word
# Output: boolean
def wonGame(correctLetters, secretWord):
    for c in secretWord:
        if (c in correctLetters) == False:
            return False 
    print("You win! The word is %s." %(secretWord))
    return True

# Determines if the user has lost the game
# Input: number of missed letters
# Output: Boolean
def lostGame(numMissedLetters): 
    if numMissedLetters == 4:
        print("Sorry, you're out of guesses.")
        return True
    return False
    # return True if numMissedLetters == 4 else False

# Propmts the user to play again
# Input: None
# Output: Boolean
def playAgain(): 
    while True:
        choice = input("Play again (y or n)? ")
        if choice in ["y","Y"]:
            return True
        elif choice in ["n","N"]:
            return False
        else:
            print("Not a valid choice.")

def main():
    printGreeting()
    playGame(readWords(input("Enter the name of file holding words: ")))
    print("Good bye!")
 
main()
