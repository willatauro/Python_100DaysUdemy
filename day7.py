#https://en.wikipedia.org/wiki/Hangman_(game)
#https://hangmanwordgame.com/?fca=1&success=0#/


'''
Generate a random word
https://developers.google.com/edu/python/lists#for-and-in
'''

import random
word_list = ["ardvark", "baboon","camel"];

chosen_word =  random.choice(word_list)

print(chosen_word)

guess = (input("Guess a letter")).lower()
print(guess)

for i in chosen_word:
    if i in guess:
        print(i)

        