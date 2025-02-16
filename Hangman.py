#Hangman
import random


def play(word):
    guessedLetters = []
    guessedWords = []
    guessed = False
    display = ""
    fullWord = "_"*len(word) #Creates placeholder for word using _

    print(fullWord)
    #User guesses first letter.
    guess = input("Enter your guess: ")
    for letter in word:
        if letter == guess:
            display += guess
        else:
            display += "_"
            guessedLetters += guess
            if len(guessedLetters) == 11:
                print("You are dead. GAME OVER")

    print(display)

# TODO:: Find location of the found letter. COMPLETE
# TODO:: Replace letters to _ and replace when found. COMPLETE
# TODO:: Check win/loss condition.
#11 Parts


#Choose random word.
words = ["Cheese","Bread"]
word = random.choice(words)
word.lower()
print(word)
play(word)
