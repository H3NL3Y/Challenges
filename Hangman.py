#Hangman
import random

def win():
    print("YOU GUESSED THE WORD!")
def hanged():
    print("YOU HAVE BEEN HANGED!")

def play(word):
    guessedLetters = []

    fullWord = "_"*len(word) #Creates placeholder for word using _
    print(fullWord)

    count = 0
    while True:
        display = ""
        guess = input("Enter your guess: ").lower()
        if guess == word: #Allows user to guess full word.
            win()
            break
        for letter in word: #Checks each letter in word.
            if letter in guessedLetters:
                display += letter #If matched it will add letter to display
            elif letter == guess:
                guessedLetters.append(guess)
                print(guessedLetters)
                display += guess
            else:
                display += "_" #If no match then add _
        count += 1
        print(display)
        if count == 7: #Provides 7 chances.
            win()
            break
        elif display == word:
            hanged()
            break

# TODO:: Find location of the found letter. COMPLETE
# TODO:: Replace letters to _ and replace when found. COMPLETE
# TODO:: Check win/loss condition. COMPLETE
# TODO:: Allow user to guess full word. COMPLETE

#Choose random word.
words = ["cheese","bread"]
word = random.choice(words)
word.lower()
print(word)
play(word)
