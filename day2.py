'''
## Data types in python

Strings -- you can get individual letter using [] called as substring, it is enclosed in quotes
Integer -- write number without quotes eg 123 or 123_256_456
Float -- 3.14
Boolean -- True or False



print(123_456_789) # to make it readable but it will print 123456789

# to check data type of a variable

num = 1234
print(type(num));

# tycasting
print(type(str(num)))
# you can typecasting str(), float(), int()


# program that adds the digits in a 2 digit number eg input 35 ouput is 8
two_digit_number = input("type a two digit number: ")

a=two_digit_number[0];
b=two_digit_number[1];

c = int(a)+int(b)
print(c)

'''
'''

Operators
+ - * /  
2**2  -- exponent 
it follows PEMDAS LR(left to right)
Parentheses exponents multiplications division addition subt



# to calculate BMI Body mass index

height = float(input("enter your hieght in m: "));
weight = float(input("enter your weight in kg: "));

bmi = int(weight/(height*height))
print(bmi)
'''
# round() -- to convert to whole number

# // floor division  you get integer -- divide gives float datatype

'''
Formating using f-string

f"your score is {score}"


score = 9
height = 9
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}");

#https://waitbutwhy.com/2014/05/life-weeks.html

#find days weeks and months left based on current age till 90

age = int(input("Whats is your current age: "))
days =(90 - age) * 365
weeks = (90 - age) * 52
months = (90-age) * 12
print(f"you have {days} days, {weeks} weeks, {months} months left")


'''

# Tip calculator project

#https://docs.python.org/3/tutorial/floatingpoint.html
#
print("Welcome to the tip calculator.");
total_bill = float(input("What was the total bill? "));
percentage_bill = int(input("What percentage tip would you like to give? 10, 12, or 15? "));
no_of_people = int(input("How many people to split the bill? "));

pay_per_person = round((total_bill + (total_bill*(percentage_bill/100)))/no_of_people,2)
pay_per_person ="{:.2f}".format(pay_per_person)
print(f"Each person should pay:{pay_per_person}")


