#PROBLEM1: Timing function execution 
#Write a decorator that measure the time a function takes to execute .

import time
def timer(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}time")
        return result
    return wrapper #wrapper is a function defined inside a decorator.

@timer#@timer is a decorator that wraps any function.


def example_function(n):
    time.sleep(n)
    
    
example_function(10)# Call the function outside, not inside its definition

#A decorator is just a function that takes another function as input, adds behavior, and returns a new function

#PROBLE2
# Debugging Function Calls(create a decorator to print the function name and the values of its arguments every time the function is called )
def debug (func):
    def wrapper(*args, **kwargs):
        args_value =', '.join(str(arg)for arg in args)
        kwargs_value=', '.join (f"{k}={v}"  for k,v in kwargs.items())
        print(f"calling:{func.__name__}with args:{args_value}and kwargs:{kwargs_value}")
        return func(*args,**kwargs)
    return wrapper
@debug
def hello():
    print("hello")
@debug    
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai",greeting ="hanji")

#def hello(): = just prepares the function in (def situation )

#hello() = calls it to actually do something (like

#CACHE RETURN VALUES 
#Implement a decorator that caches the return values of a function ,so tat when its called with the same arguments ,the cached value is returned instead of re executing the function 
import time
def cache(func):
    cache_value ={} # Dictionary to store previous results
    print(cache_value)  # Just prints the empty cache once when decorator is created
    def wrapper(*args):
        if args in cache_value:  # If input already in cache
            return cache_value[args] # return the saved result
        result = func(*args) # Otherwise, run the function
        cache_value[args]= result #Save the result in the cache
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)  # Simulates slow processing
    return a+b 

print(long_running_function(2,6))
print(long_running_function(2,6))