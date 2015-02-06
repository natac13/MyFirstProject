# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        # the get() method for dict is like indexing the dict,
        # however, return the default value(second item) if key not found
        # so freq[x] will equal the value of the key 'x' if exist +1, OR
        # it will equal 0 if x doesnt exist and then +1
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = []
    for letter in word:
        score.append(SCRABBLE_LETTER_VALUES[letter])
    if len(word) == n:
        total = ((sum(score)) * len(word)) + 50
    else:
        total = (sum(score)) * len(word)
    return total



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    # .keys() will return a list of the keys from the dict,
    # dict being the hand variable 
    # the j in range() part is the range of the value of the letter 
    # in the dict, ex. if hand['l'] returns 3 then the range is 3
    # and the letter will be printed 3 times
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,         # print all on the same line
    print ''                              # print an empty line

                                  
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    # must fill the hand with vowels first then the remainer is
    # filled by consonants
    
    for i in range(numVowels):
        # recall that random.randrange() mean from random module use the 
        # randrange() function.
        # randrange() will return an int randomly from its given range
        # x get set to the indexed char from VOWELS
        x = VOWELS[random.randrange(0,len(VOWELS))]
        # again this will set hand[x] x being the letter from vowel or
        # consonants. The get() function is for dictionaries and will return 
        # the value of hand[x] if exist or will return the default which 
        # is the second item
        hand[x] = hand.get(x, 0) + 1
        
        # so x gets set to a random 'aeiou' then I use that char to,
        # check the dict of hand to either return a value and +1, or
        # return 0 if it doesn't exist yet then add 1
        
    for i in range(numVowels, n):   
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # make copy then decrement the value for char in the word.
    # if the value returns 0 then del it, since there is no reason
    # to display to the user anymore
    x = hand.copy()
    for char in word:
        x[char] -= 1
        if x[char] == 0:
            del x[char]
    return x



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # just made copied since they should not be mutated
    xhand = hand.copy()
    xwordlist = wordList[:]
    
    # loop through the index of the word
    for i in range(len(word)):
        if word[i] in xhand.keys(): # this xhand.key() will update by del 
            xhand[word[i]] -= 1
            if xhand[word[i]] == 0:
                del xhand[word[i]]
        else:
            return False
    return word in xwordlist
    


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    ## this is my first attempt... 
    #total = 0
    #for k, v in hand.items()
    #    total += v
    #return total
    
    ## Now the one-liner!! And SUCCESS!
    return sum(v for k, v in hand.items())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # Keep track of the total score
    total = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print 'Current hand: ', 
        displayHand(hand)
        # Ask user for input
        userWord = raw_input('Enter word or a "." to indicate that '
                             'you are finished: ')
        # If the input is a single period:
        if userWord == '.':
            break
            # End the game (break out of the loop)    
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(userWord, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word,',
                print 'Please try again'
                print ''
            # Otherwise (the word is valid):
            else:
                total += getWordScore(userWord, n)
                # Tell the user how many points the word earned, 
                # and the updated total score,
                # in one line followed by a blank line
                print '"{0}" earned you'.format(userWord),
                print '{0:d} points!'.format(getWordScore(userWord, n)),
                print 'Total: {0:d} points'.format(total)
                hand = updateHand(hand, userWord)
                # Update the hand
    
    # different outcomes if the hand is now empty or not            
    if calculateHandlen(hand) == 0:
        print 'Ran out of lettters. Total score: {0:d} points'.format(total)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    else:
        print "Goodbye!",
        print "Total score: {0:d} points".format(total)

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    
    trigger = True
    while trigger:
        choice = raw_input('Enter n to deal a new hand, r to replay the '
                           'last hand, or e to end game: ')
        
        # Was able to use the exceptions!!
        # If hand is not set from the elif statement below, then an NameError
        # gets raised which I have dealt with!
        if choice == 'r':
            try:
                playHand(hand, wordList, HAND_SIZE)
            except NameError:
                print 'You have not played a hand yet.',
                print 'Please play a new hand first!'
        elif choice == 'e':
            trigger = False
        elif choice == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        else:
            print 'Invalid command.'

#
# Build data structures used for entire session and play game
# the __name__ will be set to __main__ when the script gets run from 
# the command line.
# If it gets imported it gets a _name__ of the file without extension.
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
