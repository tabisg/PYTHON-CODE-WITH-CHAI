#1.BASIC CLASS AND OBJECT 
#PROBLEM: Create a Car with attributes like brand and model .then create an instance of this class 
class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model=model

my_car= Car("toyota","corola")
print(my_car.brand)
print(my_car.model)

my_new_car= Car("tata","safari")
print(my_new_car.model)
#__init__also known as Constructor  used to initialize the object
#Class =Car and Object =my_car,my_new_car 
#2.CLASS METHOD AND SELF 
#PROB:Add a method to the Car class that displays the full name of the car (brand and model ).
class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car= Car("toyota","corrola")
print(my_car.brand)
print(my_car.model)

my_new_car= Car("tata","safari")
print(my_new_car.model)
print(my_new_car.brand)
print(my_car.full_name())
#Inheritence 
#problem :create an electirc car class that inherits from the Car class and has an additional attribute battery_size. 
class Car:
    def __init__(self,brand,model):
        self.brand= brand 
        self.model= model 
    def full_name (self):
        return f"{self.brand}{self.model}"
    
class Electriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)#We use super() to call a method from the parent class its make codes easier and shoertest 
        self.battery_size = battery_size
my_tesla =Electriccar("tesla","model S","85kwh")
print(my_tesla.battery_size)

#Encapsulation 
#problem: Modify the Car class to encapsulate the brand attribute ,making it private ,and provide a getter method for it.
class Car:
    def __init__(self,brand,model):
        self.__brand= brand # we use __(underscore )for making private  meaning it cannot be accessed directly from outside the class
        self.model= model 
    def _get_brand(self): #for this we can use brand in class but not use outside the class
        return self.__brand +"?"
    
    def full_name (self):
        return f"{self.__brand}{self.model}"
my_car = Car("Toyota", "Corolla")
print(my_car._get_brand())

class Electriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)#We use super() to call a method from the parent class its make codes easier and shoertest 
        self.battery_size = battery_size
my_tesla =Electriccar("tesla","model S","85kwh")
print(my_tesla.battery_size)
print(my_tesla.brand) #we can not use brand outside the parent class beacouse its private 


#Getter: Retrieve (get) the value of a private attribute.

#Setter: Set (update) the value of a private attribute.

#POLYMORPHISM 
#Demonstrate polymorphism by defining a method fuel_type in both Car and Electric Car classes ,but with diffrent behaviours 
class Car:
    def __init__(self,brand,model):
        self.__brand= brand # we use __(underscore )for making private  meaning it cannot be accessed directly from outside the class
        self.model= model 
    def _get_brand(self): #for this we can use brand in class but not use outside the class
        return self.__brand +"?"
    
    def full_name (self):
        return f"{self.__brand}{self.model}"

    def fuel_type(self):
        return "petrol or Diesel"
my_car = Car("Toyota", "Fortuner")
    
class Electriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)#We use super() to call a method from the parent class its make codes easier and shoertest 
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge "
my_tesla =Electriccar("tesla","model S","85kwh")
print(my_tesla.fuel_type())
print(my_car.fuel_type())
#Both Car and ElectricCar have a method called fuel_type() So its polymorphism becaouse Polymorphism lets you write one method that works differently for different objects. 

#Class Variables 
#Add a class variables to Car that keeps track of the number of cars created 
class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.brand= brand 
        self.model= model 
        Car.total_car +=1

    def _get_brand(self): 
        return self.brand +"?"
    
    def full_name (self):
        return f"{self.__brand}{self.model}"
safari=Car("Tata","Safari")
Car("Tata","Nexon")#You can also write direct Car without showing any Object
    
print(Car.total_car)

#STATIC METHOD 
#Add a static method to the Car class that returns a general descrption of a Car 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def common_fuel_types():
        return ["Petrol", "Diesel", "CNG", "Electric"]

# Static method call — does not require object
print(Car.common_fuel_types())      # Output: ['Petrol', 'Diesel', 'CNG', 'Electric']
#Suppose you are creating a voting system where you want to check if a person is eligible to vote. You can use a static method because this logic doesn't depend on any instance of the class.
class Voter:
    @staticmethod
    def is_eligible(age):
        return age >= 18

# Usage
print(Voter.is_eligible(20))  # True
print(Voter.is_eligible(16))  # False

#PROPERTY DECORATORS
#Use a property decoraters in the car class to make the model attribute read only

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model  # Use underscore to indicate "protected" attribute

    @property
    def model(self):
        return self._model  # Read-only property

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def common_fuel_types():

        return ["Petrol", "Diesel", "CNG", "Electric"]
    
my_car =Car("tata","nexon")
#my_car.model ="city" (not collable bacaouse of property decoraters you can not change the model .The @property decorator in Python is used to convert a method into a read-only attribute.)

print(my_car.model)

#CLASS INHERITENCE AND ISINSTANCE () FUNCTION 
#Demonstrate the use of isinstance() to check if my_tesla is an instance of car and electriccar
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"

# Create object of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S")

# Print details
print(my_tesla.full_name())       # Output: Tesla Model S
print(my_tesla.fuel_type())       # Output: Electric

# Use isinstance() checks
print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True
print(isinstance(my_tesla, str))          # False
#isinstance(object, class) is used to check whether an object belongs to a specific class (or its subclass).

I#t returns:

#✅ True → if the object is an instance of that class (or a subclass)

#❌ False → if not

#MULTIPLE INHERITANCE
#Create two classes battery and engine ,and let the Electric CAr class inherit from both,demonstrating multiple inheritence
# Parent class 1
class Battery:
    def battery_info(self):
        return "This electric car uses a lithium-ion battery."

# Parent class 2
class Engine:
    def engine_info(self):
        return "This electric car uses an electric motor instead of a traditional engine."

# Child class using multiple inheritance
class ElectricCar(Battery, Engine):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
# Creating object of ElectricCar
my_tesla = ElectricCar("Tesla", "Model 3")

# Accessing methods from all parent classes
print(my_tesla.full_name())        # Output: Tesla Model 3
print(my_tesla.battery_info())     # Output: This electric car uses a lithium-ion battery.
print(my_tesla.engine_info())      # Output: This electric car uses an electric motor...

# Use __init__() when:
#You need to store data in the object (like brand, model, age, price).

#Do NOT use __init__() when:
#The class only has methods (functions) and doesn't need to store data.


#Multiple Inheritance means a class inherits from more than one parent class.

#this allows the child class to use methods and properties from all parent classes
#PASS=pass is a placeholder in Python.“Do nothing here — just skip it for now without erroR.


