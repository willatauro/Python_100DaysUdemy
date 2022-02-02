#https://en.wikipedia.org/wiki/Hangman_(game)
#https://hangmanwordgame.com/?fca=1&success=0#/
'''
Generate a random word
https://developers.google.com/edu/python/lists#for-and-in
'''

import random
from day7_part3 import stages , logo
#word_list = ["ardvark", "baboon","camel"];
#import day7_part2
from day7_part2 import word_list

print(logo)

chosen_word =  random.choice(word_list)

print(chosen_word)

lives = 6

display_word =[]

# To create a word with blanks in it
for i in chosen_word:
    display_word.append('_')

# To guess till all blanks are filled

end_of_game = False

while not end_of_game:
    guess = (input("Guess a letter")).lower()
    print(guess)

  
    for position in range(len(chosen_word)):

        if guess == chosen_word[position]:
            display_word[position]= guess


    if guess not in chosen_word:
        lives-=1

        if lives == 0:
            end_of_game=True
            print("you lost")


    if '_' not in display_word:
        end_of_game = True
    
        print(display_word);
        print("You win")



print(stages[lives])