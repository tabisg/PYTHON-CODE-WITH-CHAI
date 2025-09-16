#1basic function syntax :write a function and calculate and return the square of a number 
def square(number):
    print(number**2)
    #return number**2 we also do this return (return) the number 

result =square( 9)
print(result)

#2function with multiple parameters
#create a function that takes two numbers as parameters and return their sum.

def add (numONE,numTwo):
    return numONE+ numTwo

print(add (10,10))

#3polymorphism in Function 
#write a function multiply that multiples two numbers ,but can also accept and multiply strings.

def multiply(p1,p2):
    return p1*p2 

print(multiply(5,8))
print(multiply("a",5))
print(multiply(5,"t"))
print(multiply(9,9))

#function returning multiple values 
#create a function that return both area and circumference of a circle given its radius  
import math 

def circle_stats(radius):
    #return math.pi*radius ** 2
   # print("hi") never print hi because before return the function execution is stop  so we use area as a variable
   area= math.pi*radius**2
   circumference=2*math.pi*radius 
   return area ,circumference

a, c=circle_stats(3)
print("area:",round (a,2),"circumference:",round (c,2))#round use to get only 2 digits number after point

#5default parameter value 
#write a function that greets a user .if no name is provided ,it should greet with a default name .
def greet(name ="user"):
    return "hello,"+ name +"!"

print(greet("tabis"))
print(greet())
#6Lembda function 
#Create a lambda function to compute the cube of number.
def cube(num):
    return num ** 3
cube = lambda x: x** 3 # you can directly start with lambda no need to def becouse lambda use to define quick short and clean code 

print(cube(3))
#funtion with *args 
#write a function that takes variable number of arguments and return their sum 
def sum_all(*args):#Accepts any number of values as positional arguments and they store in tuple 
    print(args)
    for i in args: #i= 1,2,3,
        print(i*2)# for multiplying value 
    return sum (args)#for adding 
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,))

#function with ** kwargs 
#Create a function that Accepts any Number of Keyword arguments and prints them in the format key value 
def print_kwargs(**kwargs): #The **kwargs allows the function to accept any number of keyword arguments (key-value pairs)
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="shaktiman",power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman",power ="lazer",
enemy="de jackaal ")

#9genrator function with yield 
#write a generator function that yields even numbers up to a specified limit 
def even_generator(limit):#yield turns a normal function into a generator ,yields give one value at a time and rembers where it left off .
    for i in  range (2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)

#Recursive Function 
#Create a recursive function to calculate the factorial of a number 
def factorial(n):
    if n==0 :
        return 1
    else :
          return n * factorial(n-1)
    
num =5
print(f"the factorial of {num} is {factorial(num)}")

    