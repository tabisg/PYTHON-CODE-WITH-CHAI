# #loops Problem in Python
# #1v1. Counting Positive Numbers
# #Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count =0
for num in numbers :
    if num >0:
        positive_number_count+=1 
print ("the positive number is ",positive_number_count)


#problem2: sum of even Numbers 
#calculate the sum of even numbers up to a given numbers n.
n=10 
sum_even =0

for i in range (1,n+1):#also we use 11 (1,11)
    if i%2 == 0:
        sum_even += 1
print ("the sum  of even numbers is : ",sum_even)
#problem3 :Multiplication of table printer 
#print the multiplication table for a given number up to 10 ,but skip the fifth iteration 
number=3
for i in range (1,11):
    if i ==5:
        continue #remove the iteration
    print (number, 'x', i , '=',number * i)
#problem4 : Reverse a String 
#Reverse a string using loop .
Input_str = "Tabis"
reversed_str=""  


for char in Input_str:
    reversed_str= char+ reversed_str
print(reversed_str)
#problem5 : Find the first Non- Repeated Character 
#given a String ,find the first non repeated character.
Input_str="teeterteetsced"
for char in Input_str :
    print(char)
    if Input_str.count(char)==1:
        print("char which is not repeated is ",char)
        break  #find first non  repeated char r then break becouse we want only first char
    #problem6 : factorial Calculator 
    #compute the factorial of a number using a while loop 
    number=5
    factorial=1
    while number >0 :
        #factorial= factorial * number
        #number=number-1
        factorial*= number
        number-= 1 
print ("Factorial numbers is ",factorial)
#problem7 :validate input 
#keep asking the user for input untill they enter a number betweeen 1 and 10
xna = 5
while(xna > 0 ) :
    number= int(input("enter the value b/w 1 and 10 "))
    if 1 <= number <=10:
        print ("thanks ")
    else :
        print("the number is invalid ")
    xna = xna -1
#problem 8 : check if a number is prime 
number= 30 
its_prime =True
if number >1 :
        for i in range (2, number):
            if (number % i)== 0:
                its_prime= False
                break 
print (its_prime)

#problem 9. List Uniqueness Checker
#Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate 

items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set ()
for item in items :
    if item is unique_item:
         print("duplicate ",item)
    break
unique_item.add(item)

#10Exponential Backoff 
#implement an exponential backoff strategy that doubles the wait time between retries starting from 1 second ,but stop after 5 retries 
import time 
wait_time = 1
max_tries =5 
attempts= 0 

while attempts < max_tries :
    print("Attempt",attempts+1 ,"wait time",wait_time,)
    time.sleep(wait_time)
    wait_time*=2
    attempts+= 1