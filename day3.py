#conditional statements
'''
if condition:
    do this
elif conditon:
    do this
else :
    do this

draw.io to create flow chart

comparison operators >, <, >=, <=, ==, !=


#Program to check odd or even

number = int(input("Enter a number you want to check "))

if number==0:
    print(f'The {number} number is neither odd or even')
elif number%2==0:
    print(f'The number {number} is even')
else :
    print(f'The number {number} is odd')



#Improved BMI Calculator

height = float(input('Enter your height in m: '));
weight = float(input('Enter your weight in kg: '));

bmi = round(weight/(height**2))

print(f'Your BMI is {bmi}');

if bmi<18.5:
    print(f'Your BMI is {bmi}, you are underweight')
elif bmi>18.5 and bmi<25:
    print(f'Your BMI is {bmi}, you have a normal weight' ) 
elif bmi>25 and bmi <30:
    print(f'Your BMI is {bmi},you are overweight')
elif bmi>30 and bmi <35:
    print(f'Your BMI is {bmi},you are obese')
else:
    print(f'Your BMI is {bmi},you are clinically obese')



#Write a program that works out whether if a given year is a leap year
#https://www.youtube.com/watch?v=xX96xng7sAE&ab_channel=CGPGrey
#https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf

year_check = int(input("Enter the year to check if leap year or not: "))


if year_check%4==0:
    
    if year_check%100==0:
        if year_check%400==0:
            print(f"The year {year_check} is leap year");
        else :
            print(f"The year {year_check} is not a leap year");
    else:
        print(f"The year {year_check} is leap year");    

else:
    print(f"The year {year_check} is not a leap year");

if/elif/else

# Here only one condition will be executed
if condition1:
    do A
elif conditon2:
    do B 
else: 
    do C

# Multiple if -- Here all the condition will be evaluated
if condition1 :
    do A 
if condition2:
    do B 
if condition3:
    do c 



#Pizza order 

print("Welcome to Python Pizza Deliveries!");

size = input("What size pizza do you want? S, M, L: ");
add_pepperoni = input("Do you want pepperoni, Y or N: ");
extra_cheese = input("Do you want extra cheese, Y or N: " );

bill =0

if size=='S':
    bill = 15;
    if add_pepperoni =='Y':
        bill = bill +2;
if size =='M':
    bill = 20;
    if add_pepperoni =='Y':
        bill = bill + 3;

if size == 'L':
    bill =25;
    if add_pepperoni =='Y':
        bill = bill + 3;

if extra_cheese =='Y':
    bill = bill + 1;

print(f"The bill is ${bill}")


# The above code can be written in a better way

print("Welcome to Python Pizza Deliveries!");

size = input("What size pizza do you want? S, M, L: ");
add_pepperoni = input("Do you want pepperoni, Y or N: ");
extra_cheese = input("Do you want extra cheese, Y or N: " );

bill =0

if size=='S':
    bill += 15;

elif size =='M':
    bill += 20;

elif size == 'L':
    bill += 25;

if add_pepperoni =='Y':
    if size =='S':
        bill += 2;
    else :
        bill += 3
if extra_cheese =='Y':
    bill += 1;

print(f"The bill is ${bill}")
   

#https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day%203%20Logical%20Operators.drawio#R7VtZc9o6FP41zH2iY0teH0uWZpqkQy%2BZ29CXOwYrthNjUVkQyK%2BvjGWwLbEFL6HTzCSxjyVhfec7myQ68GKy%2BEKcqX%2BPXRR2gOIuOvCyA4CqAYP9SyTLVGJqXOCRwOWNNoJB8Ia4UOHSWeCiuNCQYhzSYFoUjnEUoTEtyBxC8Gux2RMOi586dTwkCAZjJxSlPwKX%2BqnUAuZGfoMCz88%2BWTXs9MnEyRrzmcS%2B4%2BLXnAhedeAFwZimV5PFBQoT8DJc0n7XW56uX4ygiB7SoR9ZTw%2FfyQD19fm%2Fc3dxF%2FzCXT6NmC6zCSOXzZ%2FfYkJ97OHICa820h7Bs8hFyagKu9u0ucN4yoQqEz4jSpdcmc6MYiby6STkT9kLk%2BVj0v%2BTAUEmGDJBV%2FmkmHomuVzwz0jvlvm7PiLBBFFEuFBEgwMU4xkZox0QZKxyiIfojnZ62i7BJ%2FcBHOsvCLO3IUvWgKDQocG8yB%2BH09Bbt%2BNdPxPiLHMNpjiIaJwbuZ8IWANuUZABthqR25Oq63mts4t0xOwu92ob0YoZR7DEbpklmqrlWaJ8TIJotRBEYICqFQlgK8UR0vfknTbMOJZohtE8zzgWcyeccXS4b01cm%2BFMGHF6Hl0pU1GZz5904LVATeLjyWjGZtl79QOKBlNnpd1XFp%2BKBNvKiDkiFC126jB7qppFlLKw9bqJFarBZX4uTpSVlld7DuPjIYRtmOr7bQscaFtq1bZ1EshA4OmAzYCKVFwDq%2B6n41MQhhc4xGTVF7o6stzE7cWU4BeUe2KBEWTWWQ2BYZHAQMJfIOGvVhd%2FNQHaCyf6J%2FEALD1EpyFcAV5QKcIlsXfLrAeuy682%2BL%2F%2FzaXPLvk%2BvOl71zdexsRzMXddNHfptD6WuesyTn4URgKzZMENUlLuqhUBrm9YgInNjhaxcMLAi9j1mGGRZG29BIOAVWKf%2BYNJ4LopgVEcvDmj1VAJhXkqw8bVex39MhmLcTZO6VsRzFYp0ENbQBlK%2FCSoDWUxVxqi%2BOxhBpa2F2etJpylnkiMR2143FwttK6OD6mEDvLUuzzwXk9tVO2p5dUIUJKZ55kBgV4cZEvd847aRA6I8lfx%2BXZWWyFa%2FtZ%2FzbLQzm4tgVKGP3%2B8PfT6PwfImj8%2BPAS9STtZKloE9DF3Pdzoid1tNJPcFFaO2laoFMLWMuJdb52LiskyepsrMcASAoQiSYQlqYNeW23Wsk9qhsD1JADHrlaqsKh8zSpthpTzCRvual9c3tzbWy8XUzXnIoYkKWUq1HTRBBuuRu3i%2Bgi0RBu0a1pOkiJlCkjdoThOHK6%2FKuElecO5lUxqGfMD%2FV5tJRNoJVN%2BvwerPJPdsnMHyhFKL6ugZrdhbXEb4iZw84tYejl6t%2B051vRpJ3qrzUTvyuuEd0VvXTkuekPNOiF6l3s3Hb3tLWYoiUVN26FmfLD4LVnmVEFXtc4%2BakNV8Hi6iLXeZNxWoYg1A1rBJPnDpnb%2BoB%2BQKpmNpkqyTH6rD1D2%2BwBhs9gYW2j0VNpejnCUqMB1Yn%2FtXCqAVzeL8AKJ91Bl%2BK6PSJwCsH3%2F%2BGI8erfgFvwKlvfPN8v%2BfVekdBtR%2FaD4vGvZJ7885M%2FnXfx0iYKv9n%2Bz5a06uDNesnnWncPqalHDh2awRx8%2BsuSZcmWnj3ZgLcRlsZxpOiwbWnthWQqVaFafPYYHUJIlCKXLfnVxLeLcooVuvm9BsYpoITXyViqSg3zXLp%2B013dVfrD2JJBbCRDZXkW2IXHkXgWofrPiJI2aH0qjorN6dSJ%2BpjRMPNKIZbbG6lzp1MfMi5x0qlTIwJTVjzwDq8BLlQ%2FqrkNyPulSbNFNWXW5Ka1VC1pbzTD3pIXdvl2u7swMSDz%2FliZG4lnjoxKjpi0FlnZtDNlhbaWmNEoKrFj9%2FQlnuMo4r9fXGjjDtcuacjA%2F%2BCgxQ0ydpPMoSMeIVzFBW5wXrVmeWoDblKSpKrCz1aZGiC3uNPwBR0ABLEVaCa8rOgPKbjdfDEzr283XK%2BHVbw%3D%3D

Logical Operators

A and B 
c or D 
not E 

print("Welcome to Roller coster")

height = int(input("enter you height in cm: ")) ;
age = int(input("enter your age")) ;
price =0;
if height > 120:
    if age <12:
        price += 5;
    elif age <18:
        price += 7;
    elif age >= 45 and age <=55:
        print("No need to pay")
    else :
        price += 12
        
    want_photo =input("Do you want photos Y or N: ")

    if want_photo == 'Y':
        price += 3

else:
    print("You can't ride");

print(f"The total bill is ${price}");


You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"
#https://replit.com/@ZeroPatch/day-3-5-exercise-1#main.py


print ("Welcome to the love calculator!")

name1 = input("Enter your name? \n");
name2 = input("Whats is their name? \n");


score1 = 0
score1 += name1.lower().count("t") + name2.lower().count("t")
#print ("count t",score1)
score1 += name1.lower().count("r") + name2.lower().count("r") 
#print ("count r",score1) 
score1 += name1.lower().count("u") + name2.lower().count("u")
#print ("count u",score1)
score1 += name1.lower().count("e") + name2.lower().count("e")
#print ("count e",score1)
print (score1)

score2 = 0
score2 += name2.lower().count("l") + name1.lower().count("l")
score2 += name2.lower().count("o") + name1.lower().count("o")
score2 += name2.lower().count("v") + name1.lower().count("v")
score2 += name2.lower().count("e") + name1.lower().count("e")
 
print(score2)

total = str(score1) + str(score2)

if int(total) <10 or int(total) >90:
    print(f"your score is {total}, you go together like coke and mentos.")

elif int(total) >= 40 and int(total) <=50:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"your score is {total}") 

    # you can combine the string like name+name2, convert to lower, than count, instead of score you can do count t, r,u, e then say t+r+u+e

    #https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#https://ascii.co.uk/art
''' 

print('''
                     __
          ..=====.. |==|
          ||     || |= |
       _  ||     || |^*| _
      |=| o=,===,=o |__||=|
      |_|  _______)~`)  |_|
          [=======]  ()       ldb
''')
print('Welcome to treasure island')

choice = input("Enter left or right? ");

if choice.lower() =="left":
    choice2=input("Do you want to swim or wait: ")

    if choice2.lower()== "wait":
        choice3 = input("Whic door, Red, yellow, blue or your choice");

        if choice3.lower() =="yellow":
            print("You win!");
        elif choice3.lower() =="blue":
            print("eaten by beast")
        elif choice3.lower() =="red":
            print("Burned by fire")
        else:
            print("Game Over")
    else:
        print("Attacked by trout! Game over")
else:
    print("Fall in hole: Game over")


