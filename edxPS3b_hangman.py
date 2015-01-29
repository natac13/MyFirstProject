# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
''' this is a game of hangman, very simple!
    there is a list of words added and then randomly selected,
    at which point the game starts.
    8 guesses, with no chance to guess the word,
    I point that out since I changed tht in my version of the game
    '''

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string #### Could also be read() however all word on same line
    line = inFile.readline()
    # wordlist: list of strings the string part is what to split on
    # if blank or as it is written then .split on spaces
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    # Create a list version of secretWord so I can removed 'found' letters
    x = [x for x in secretWord]
    for i in x[:]:
        if i in lettersGuessed:
            x.remove(i)
    return len(x) == 0


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    # Check if the letter in the secretWord is in lettersGuessed
    # Build a list of either the letter guessed or a "_ "
    output = []
    
    for i in secretWord:
        if i in lettersGuessed:
            output.append('{}'.format(i))
        else:
            output.append('_')
    return ' '.join(map(str, output))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    x = list(string.ascii_lowercase)
    
    for i in lettersGuessed:
        if i in x:    ## this was added since I got an error when updating var.
            x.remove(i)
    return ''.join(map(str, x))

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
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game hangman!"
    print "I am thinking of a word that is {0:d} letters long.".format(len(secretWord))
    
    guesses = []
    attempt = 8
    main_word = secretWord
    
    
    while not isWordGuessed(main_word, guesses) and attempt > 0:
        # able to update the string of available letter 
        choose_from = getAvailableLetters(guesses)
                 
        print '-' * 13
        print "You have {0:d} guesses left.".format(attempt)
        print "Available letters: {0}".format(choose_from)
        
        current_guess = raw_input("Please guess a letter: ").lower()
        guesses.append(current_guess)
        output_update = getGuessedWord(main_word, guesses)
        ## check to see if in main_word and the available letter
        if guesses[-1] in main_word and guesses[-1] in choose_from:
            print "Good guess: {0}".format(output_update)
        elif not guesses[-1] in choose_from or guesses[-1] in main_word:
            print "Oops! You have already",
            print "guessed that letter: {0}".format(output_update)
            attempt -= 1
        else:
            print "Oops! That letter is",
            print "not in my word: {0}".format(output_update)
            attempt -= 1
    
    print '-' * 13
    
    if isWordGuessed(main_word, guesses):
        print "Congratulations, YOU WON!"
    else:
        print "Sorry you ran out of guesses. The word was {0}".format(main_word)
            


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
