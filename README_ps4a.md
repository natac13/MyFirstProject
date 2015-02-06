Jan 27, 2015

## For getWordScore

* first I make an empty list to be able to collect the values of the letters
* I get these values by using a for loop to go through each letter 
  in the word and grab from the SCRABBLE_DICT the cosponsoring score
* Then I find out with an if statement if word is the same length as n, 
  which means all the letters were used and therefore the extra 50 points 
  is applied. 
* So I make a total and set it equal to the computation of scoring based
  on the rules(SCRABBLE_DICT letter score summed multiplied by length, and 
  plus 50 points if all letter used)
* returning the value at the end
* Time taken was around 15 minutes, and passed the test_ps4a.py file!

# I started looking over the pre-made code for problem #2.
# This lead me to make make a different branch using git, and I called 
  it ProblemTwo. I will make my problem #2 changes here and then try my best
  not to screw up the merge to the master when i feel the code is ready!!
* I believe this is how people use version control however I still do not fully 
  grasp the concept but working on it!!
  
Jan 28, 2015

* MEGERED the ProblemTwo branch with the master branch. I made sure
  to make a copy of the original master branch which is in a folder call temp, 
  at the same level as 6.00.1. 
* Can probably delete this, since I now think that I leave the master 
  alone and work on new branch when I want to change things.
  Once I become happy with these changes and feel they are really working, 
  then I merge with the master branch.
** My next thing to attempt is to have a master then to different branches, 
  with different changes and then see what happens when I merge both to 
  master, to see if they both just add to the master.
  
## Problem 2 

* After looking over the pre-made code and writing comment to explain 
  it to myself further(maybe a bit too verbose), I worked on the displayHand().
* It seemed very simple to implement. I looked over the test code, 
  which shows the answer could be either filled with just remaining letter, 
  or with all the original letter and 0 values. 
* I didn't like the latter which I first came up with.
* Added the del statement to deal with this annoyance!

## Problem 3

* I think it was pretty straight forward. Meaning I just made copies, 
  of the object which should not be changed. They checked if the characters
  in the word were in the keys of the dict hand, the minus 1 from there values.
  All done on a copied version of the dict object
* If the value became 0 then I delete the key so that the "for x in dict.keys()"
  part is being mutated during the process of checking. This accounts for 
  the pesky user from using the same letter twice to make a word!


Jan 29. 2015
  
## Finished the playHand and playGame functions.

* Game is now playable
* The pre-made pseudo-code that was provided was VERY helpful with my thought
  processing throughout the code writing
  I really need to start do this with my own projects
* I was able to understand (and therefore use in my code!!) how to handle
  exceptions when they come up. Like if I try to call the playHand() before
  hand variable is set there is a NameError. I code a way to deal with this
  and print out statements to inform the user of the mistake.
* After the user plays one hand the exception will not get raised again, which
  is exactly how the game is to be implemented!  


## Computer chooses a hand

* Thought this was going to be harder then it really was.
  just had to change the isValidWord() a bit to just return for finish iterating
  over the word variable
* In the end I had the computer look at every word in the list, then if the 
  character in each word appear in the hand I do the removing of values and 
  deleting of the keys to a copied version. Then call getWordScore()
* Doing a simple check to see if the current_word is a larger score then 
  max_score, if that happens I update the max_score and change the chosen 
  word to the current_word.
* After going through the entire list the computer will return the best_word