#https://en.wikipedia.org/wiki/Mersenne_Twister
#https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random
'''
random_int = random.randint(0,5)
print(random_int)

random_float = random.random()
print(random_float+random_int)
print(random_float*5)  # preferred way to print random decimal numbers between 0 and 5

#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".


rand_int = random.randint(0,1)

if rand_int ==1:
    print("Heads")
else:
    print("Tails")

#https://docs.python.org/3/tutorial/datastructures.html


#List : data structure to store items that are related or can be grouped, its a ordered list and you can call out the items using index

#append will add a single item at the end of the list, extend adds a list of items to the end of existing list


# Programming is like open book exam you should not memorize it rather solve problems 

#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

#https://www.askpython.com/python/string/convert-string-to-list-in-python
#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
#https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/



names_string = input("Give me everybody's name separated by comma: ")
names = names_string.split(", " )
print(names)

length_of_names = len(names)

rand_int = random.randint(0,length_of_names-1)

print(f"{names[rand_int]}, will pay the bill");


print("Welcome to Treasure Map!")

row1 = ["🥸","🥸","🥸"]
row2 = ["🥸","🥸","🥸"]
row3 = ["🥸","🥸","🥸"]


#nested list, that is lis within list
map =[row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
 
mark_row = int(input("Enter the row: "))
mark_col = int(input("Enter the col: "))


map[mark_row][mark_col]="X"



position = input("Enter the vertical and horizontal postion")

map[int(position[0])-1][int(position[1])-1] ="X"

print(f"{row1}\n{row2}\n{row3}")
'''
#https://wrpsa.com/

'''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print(rock)
print(paper)
print(scissors)

print("Welcome to Rock Paper Scissors")

choice_you = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))

choice_comp = random.randint(0,2)

games_images = [rock,paper,scissors]


print(f"you chose{games_images[choice_you]}")

print(f"computer chose{games_images[choice_comp]}")

if choice_you ==0 and  choice_comp ==2:
    print("You win")
elif choice_you ==2 and  choice_comp ==1:
    print("You win")
elif choice_you ==1 and  choice_comp ==0:
    print("You win")
elif choice_you == choice_comp ==0:
    print("Draw")
else:
    print("You lose")