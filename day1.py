''' 
# ''' #is an multi-line comments and # is single line comment
'''
# strings in single quotes
print('Hello world');

# strings in Double quotes
print("Hello world!")

#stackoverflow is the website to goto for answers
# to use single quotes inside double quotes an vice versa
print("print('what is print')");

#new line
print("Hello world \nWilander");

#String concatenation
print ("Hello World" + " Wilander")

# Input function

#print('whats your name', input());
# Similar to print it waits for user to enter the input
#input("Whats your name?");


#print('whats your name')
#input() will execute first get the value and then replace in print statement
#input('prompt or message for the user to enter input')
#Thonny -- to see how computer evaluates the step free application for python
print('Hello '+ input('Whats your name'))

# to get length of name

print('the length of your name is ' + str(len(input("Enter your name"))))


# variables, below name is a variable

name = input('whats your name')
print(name)


# Switch the variables, program that switches values stored in variables a and b
# variable name cant start with number and it cant have a space in it, variable are case sensistive 
a = input('enter a ');
b= input('enter b ');

c=b
b=a
a=c

print('the value of a is: ', a);
print ('the value of b is: ', b)
'''
print("Welcome to Band Name Generator.")
city=input("What's name of the city you grew up in? \n" );
pet= input("What's your pet's name?\n");

print('Your band name count be ' +city +" "+pet);