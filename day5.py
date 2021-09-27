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
'''
 #write a program that calculates the sum of all the even numbers from 1 to 100
# other way is range(2,101,2) make the step size to 2

sum = 0
for n in range(1,101):
    if n%2==0:
        sum += n
print(sum)
