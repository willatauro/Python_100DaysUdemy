'''
def greet(a): #parameter
    print("Hello "+ a)
    print(f"Hello {a}")

name = input("What's your name:")
greet(name)  # argument


# Positional arguments
def greet_nam_loc (a,b):
    print(f"Hi {a}, how's the weather in {b}")

name = input("enter your name")
loc = input("enter your location")

greet_nam_loc(name,loc)


#Keyword arguments 

def greet_nam_loc (a,b):
    print(f"Hi {a}, how's the weather in {b}")

name = input("enter your name")
loc = input("enter your location")

greet_nam_loc(a=name,b=loc)

import math
height = int(input("enter height of the wall"))

width = int(input("enter width of the wall"))

coverage = int(input("Enter coverage of can"))

def numofcans(h,w,c):
    numberofcans = math.ceil((h*w)/c)
    return numberofcans 

num = numofcans(h=height,w=width,c=coverage)

print(f"The number of cans is {num}")


# Prime number checker , a number is prime if its only divisible by itself and one
'''
#for instance 7
#7%2 = 0 --- not a prime
#7%3 = 0 --- not a prime
#7%4 = 0 --- not a prime
#7%5 = 0 --- not a prime
#7%6 = 0 --- not a prime
'''
 
from operator import truediv


def prime_checker(n):

    is_prime = True
    for i in range(2,n):


        if n%i == 0:
            is_prime =False
        
    if is_prime:
        print("number is prime")

    else:
        print("number is not prime")    



num = int(input("enter the number to check"))

prime_checker(num)
'''

#https://www.w3schools.com/python/ref_list_index.asp

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt and 'decode' to decrypt")

txt = input("Enter the text message: \n").lower()

shift = int(input("Enter the shift key: \n"))


def encrypt(plain_text,shift_amount):
    
    cipher_txt =""
    for letter in plain_text:
       position = alphabet.index(letter)

       if position+shift_amount >=26:
           new_position = shift_amount-1
       else:
            new_position = position + shift_amount
       new_letter = alphabet[new_position]
       cipher_txt +=new_letter
    print(f"The encoded message is {cipher_txt}")


def decrypt(cipher_txt,shift_amount):
    
    plain_txt =""
    for letter in cipher_txt:
        position = alphabet.index(letter)
        if position +shift_amount >=26:
            new_position = 26-shift_amount-1
        else:
            new_position = position -shift_amount
        new_letter =alphabet[new_position]
        plain_txt += new_letter
    print (f"The decoded message is {plain_txt}")
if direction =='encode':
    encrypt(plain_text=txt, shift_amount=shift)

if direction =='decode':
    decrypt(cipher_txt =txt , shift_amount=shift)
