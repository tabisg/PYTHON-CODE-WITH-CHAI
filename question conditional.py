#10 conditional problems in python
#1.Age group Categorization :child(<13),Teenager(13 to 19),Adult(20-59),senior(60+)

age=80
if age <13 :     
    print ("child")
elif age <20:
    print("teenager")
elif age<60 :
    print("adult")

else :
    print ("senior")


#v2. Movie Ticket Pricing
#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age=90
day= "wednesday "
price= 12 if age >=18 else 8 #12 if age is greater than or equal to 18 else 8
if day == "wednesday ":
    price=price-2
print ("ticket price for you in $ ",price)

#you can run this code in diffrent way 
age = 90
day = "wednesday "

if age >= 18:
    price = 12
else:
    price = 8

if day == "wednesday ":
    price -= 2

print("ticket price for you in $", price)

#Grade Calculator : Assign a letter base on a Studnet's score =A(90-100),B(80-89),C(70-79),D(60-69),F(below60). 

score=200
if score >=101:
    print("Please verify your Score Again  ")
    exit()

if score >=90:
    Grade= "A"
elif score>=80:
    Grade= "B"
elif score>=70:
    Grade="C"
elif score>=60:
    Grade="D"
else :
    Grade="F"
print (Grade ,"grade")

#Fruit Ripeness Checker :Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe Yellow - Ripe, Brown - Overripe)

fruit="Banana"
color ="green"

if fruit == "Banana":
    if color == "yellow":
        print(fruit , "Ripe") 
    elif color == "green":
        print(fruit ,"Unripe") 
    elif  color == "Brown":
        print(fruit , "overripe")
#Weather Activity Suggestion :Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book,Snowy - Build a snowman)
weather="Rainy"


if weather=="Sunny":
    print("go for a walk ")
elif weather=="Rainy":
    print("read a Book")
elif weather=="Snowy":
    print("Build a snowman ")
else:
    print("normal weather ")

#we do same code in a diffrent way like 
weather="winter"
if weather=="sunny":
    activity=("go for a walk ")
elif weather=="Rainy":
    activity=("read a Book")
elif weather=="Snowy":
    activity=("Build a snowman ")
else:
    activity=("nothing ")

    print(activity)

#Transportation Mode Selection :Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)
distance= 1000
if distance >=900:
        print("car is stop")    
        exit()
if distance <3:
    transport = "walk"
elif distance <=15:
    transport= "Bike"
elif distance >15:
     transport="Car"    
else:
    transport=("flying")
print("AI recomend you to transport of ",transport)

#Coffee Customization :Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
order_size="large"
Extra_shot= True

if Extra_shot :
  coffee = order_size +"coffe with an extra shot"
else:
   coffee= order_size + "coffee"
    
print("order :",coffee)

#Password Strength Checker:Check if a password is "Weak', "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password= "123tabish"
password_len=len(password)

if len(password)<6:
    strengt=("weak")
elif len(password)>=10:
    strenght=("medium")
else:
    strength=("strong")
print("password strenght is :",strenght)

#VLeap Year Checker Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400

year =2024

if (year % 400== 0) or (year % 4== 0) and (year %100 != 0):
   
    print(year ,"is leap year ")
else:
    print(year,"not leap year ")

