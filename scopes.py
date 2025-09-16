username="chaiaurcode" #global variable 

def func ():
   # username= "chai" "if function not get username from global scope then it will create a memory spece for username in local scope "
    print(username)


print(username)    
func()

x=99
def func2(y):
    z=x+y # x s a global variable  just like username 
    return z 

result=func2(1) #1 is a local variable 
print(result) #99+1 =100 becouse x is a global vaariable and y is a local variable 

#if you want to uuse global variable in function then you have to use global key before variable name 
def func3():
    x=88 

print(x) #99 becouse x is a global variable and first print x then it will print global variable 



def func4():
   global x # x is a global variable use to acess gloal variable in function and also for changing the global variable value
   x=12 # change the value of global variable x
func4()
print(x)


def f1():
   x=88
def f2():
    print(x)
    return f2
myResult= f1()
myResult()#88


def outer(msg):
    def inner():
        print(f"hello vishal jhatu : {msg}")
    return inner

greet = outer("Hello from closure!")
greet()  # Output: Message: Hello from closure!

#closer or factory function is function that returns another function called closure wheich can access the variables of the outer function even after the outer function has finished execution

#climing in function is called when you want to use global variable in function if function is not found then it will give error 