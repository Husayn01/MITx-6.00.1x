# Now you will implement the function hangman, which takes one parameter - 
# the secretWord the user is to guess. This starts up an interactive game of 
# Hangman between the user and the computer. Be sure you take advantage of the three helper functions, 
# isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) 
# to load the words and pick a random one. Note that the functions loadWords and 
# chooseWord should only be used on your local machine, 
# not in the tutor. When you enter in your solution in the tutor, 
# you only need to give your hangman function.
                                                                                                                                                                                                                   
# Consider using lower() to convert user input to lower case. For example:

# guess = 'A'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
# guessInLowerCase = guess.lower()                                       
# Consider writing additional helper functions if you need them!

# There are four important pieces of information you may wish to store:
                                                                                                                         
# secretWord: The word to guess.
# lettersGuessed: The letters that have been guessed so far.
# mistakesMade: The number of incorrect guesses made so far.
# availableLetters: The letters that may still be guessed. 
# Every time a player guesses a letter, the guessed letter must be removed from 
# availableLetters (and if they guess a letter that is not in availableLetters, 
# you should print a message telling them they've already guessed that - so try again!).

import string

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    mistakesMade = 0
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")

    while True:
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        if mistakesMade >= 8:
            print("Sorry, you ran out of guesses. The word was", secretWord + ".")
            break

        print("You have", 8 - mistakesMade, "guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters:", availableLetters)
        guess = input("Please guess a letter: ").lower()

        # Validate input
        if len(guess) != 1:
            print("Oops! Please enter a single letter.")
            print("-------------")
            continue
        if guess not in string.ascii_lowercase:
            print("Oops! That is not a valid letter.")
            print("-------------")
            continue

        # Check if the letter has already been guessed
        if guess in lettersGuessed:
            currentGuessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter:", currentGuessedWord)
            print("-------------")
            continue

        # Process the new guess
        lettersGuessed.append(guess)
        currentGuessedWord = getGuessedWord(secretWord, lettersGuessed)

        if guess in secretWord:
            print("Good guess:", currentGuessedWord)
        else:
            print("Oops! That letter is not in my word:", currentGuessedWord)
            mistakesMade += 1

        print("-------------")

# Helper functions (as provided in the problem statement)
def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    word = ["_"] * len(secretWord)
    for index, letter in enumerate(secretWord):
        if letter in lettersGuessed:
            word[index] = letter
    return " ".join(word)

def getAvailableLetters(lettersGuessed):
    alphabet = string.ascii_lowercase
    return ''.join([letter for letter in alphabet if letter not in lettersGuessed])