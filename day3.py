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

'''

#Improved BMI Calculator

height = float(input('Enter your height in m: '));
weight = float(input('Enter your weight in kg: '));

bmi = weight/(height**2)

print(f'Your BMI is {bmi}');

if bmi<18.5:
    print('Under') 