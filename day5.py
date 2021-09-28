#Loops
#haveibeenpwned.com
#Welcome to password generator

# for item in list_of_items

#program that calculates the average student height from a List of heights. wihout using sum and len functions
'''
student_heights = input("Enter the student heights separated by space eg 100 110 : ").split()
sum=0 
m=0
for n in student_heights:
    print(n)
    sum = sum + int(n)
    m= m+1

print(sum)
print(m)
print(f"The avg height is {sum/m}")

#second way

total_height = sum(student_heights)
number_of_students = len(student_heights)
avg_height = round(total_height/number_of_students)
print(avg_height)

#for n in range(0, len(student_heights)):
  #student_heights[n] = int(student_heights[n])




#write a program that calculates the highest score from a List of scores


student_scores = input("Input a list of student scores ").split()
print(student_scores)
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max = 0
for n in student_scores :
    if n > max:
        max=n
print(f"the highest score is: {max}")



#range  range(a,b) its between a and b not including  b
sum =0
for n in range(1,101):
    sum += n

print(sum)

 #write a program that calculates the sum of all the even numbers from 1 to 100
# other way is range(2,101,2) make the step size to 2

sum = 0
for n in range(1,101):
    if n%2==0:
        sum += n
print(sum)

#FizzBuzz
print("Welcome to FizzBuzz problem")

for i in range(1,101):

  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print ("Fizz")
  elif i%5==0:
    print ("Buzz")
  else:
    print(i)
'''

import random
print("Welcome to PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many leters would you like in your password: "))
nr_sym = int(input("How many symbols would you like? "))
nr_num = int(input("How many number would you like? "))

# Create a list and use append and random to pick up random indexes from list
pwd =[]
for l in range(1,nr_letters+1):
  #pwd.append(letters[random.randint(0,l)])
  pwd.append(random.choice(letters));
  
for s in range(1,nr_sym+1):
  pwd.append(random.choice(symbols))

for n in range(1, nr_num+1):
  pwd.append(random.choice(numbers))
  
#print(pwd)
# shuffle the list
random.shuffle(pwd)
#print(pwd)

# Covert list to string
password =""

for char in pwd:
  password +=char
print(password)