#Task 1: First-Class Function Warm-Up
#•  Demonstrate that functions are first-class objects in Python by: (a) assigning a function to a new
#variable and calling it through that variable, (b) passing a function as an argument to another
#function, (c) returning a function from another function.
#•  This task does not use @decorator syntax; it only prepares the concepts needed for it.

def greet(name):
    return f"Hello, {name}!"


# Assign the function to another variable
new_greet = greet

# Call the function through the new variable
print(new_greet("Alice"))

#output:Hello, Alice!

def square(number):
    return number ** 2


def apply_function(function, value):
    return function(value)


result = apply_function(square, 5)

print(result)
#output:25

def create_multiplier():
    
    def multiply_by_two(number):
        return number * 2

    return multiply_by_two


# Get the returned function
multiplier = create_multiplier()

print(multiplier(10))

#output:20

#Task 2: A Basic Logging Decorator
#•  Write a decorator log_call that, when applied to any function, prints the function's name and its
#arguments before calling it, and prints the return value after the call.
#•  Apply @log_call to a simple add(a, b) function and test it.

def log_call(function):
    def wrapper(*args, **kwargs):
        print("Function name:", function.__name__)
        print("Arguments:", args)

        result = function(*args, **kwargs)

        print("Return value:", result)

        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


# Test the decorated function
result = add(5, 3)

print("Result:", result)

#output:Function name: add
Arguments: (5, 3)
Return value: 8
Result: 8

#Task 3: Execution Time Decorator
#•  Write a decorator timer that measures and prints how long the decorated function takes to
#execute, using the time module.
#•  Apply it to a function that performs a computationally heavy task (e.g. summing numbers in a large
#range) and observe the timing output.

import time
from functools import wraps


def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"{function.__name__} took {elapsed_time:.6f} seconds")

        return result

    return wrapper


@timer
def calculate_sum():
    total = 0

    for i in range(10_000_000):
        total += i

    return total


result = calculate_sum()
print("Sum:", result)

#output:calculate_sum took 0.523417 seconds
#Sum: 49999995000000


#Task 4: Decorator with Arguments
#•  Write a parameterised decorator repeat(n) that, when applied to a function, calls the decorated
#function n times in a row each time it is invoked.
#•  Apply @repeat(3) to a function that prints a greeting, and verify it prints the greeting three times
#per call.

from functools import wraps


def repeat(n):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for i in range(n):
                function(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello! Welcome to Python.")


greet()
#output:Hello! Welcome to Python.
#Hello! Welcome to Python.
#Hello! Welcome to Python.

#Task 5: Access-Control Decorator
#•  Write a decorator require_login that wraps a function and only allows it to execute if a global
#variable is_logged_in is True; otherwise it should print an access-denied message and not call the
#function.
#•  Demonstrate the decorator's behaviour both when is_logged_in is True and when it is False.
#•  Use functools.wraps in this decorator and explain in your record why it is good practice to use it.

from functools import wraps

is_logged_in = False


def require_login(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return function(*args, **kwargs)
        else:
            print("Access denied. Please log in first.")

    return wrapper


@require_login
def view_profile():
    print("Welcome to your profile!")


# Test when the user is NOT logged in
print("When is_logged_in = False:")
view_profile()


# Test when the user IS logged in
is_logged_in = True

print("\nWhen is_logged_in = True:")
view_profile()

#output:When is_logged_in = False:
#Access denied. Please log in first.

#When is_logged_in = True:
#Welcome to your profile!
#Task 6: Stacking Multiple Decorators
#•  Apply both @log_call (from Task 2) and @timer (from Task 3) to the same function, stacked on
#top of each other.
#•  Run the program and note the order in which the decorators' effects appear in the output; explain
#why that order occurs

import time
from functools import wraps


def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Function name:", function.__name__)
        print("Arguments:", args)

        result = function(*args, **kwargs)

        print("Return value:", result)

        return result

    return wrapper


def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        print(f"Execution time: {end_time - start_time:.6f} seconds")

        return result

    return wrapper


@log_call
@timer
def add(a, b):
    return a + b


result = add(10, 20)

print("Final result:", result)
#output:
#Function name: add
#Arguments: (10, 20)
#Execution time: 0.000002 seconds
#Return value: 30
#Final result: 30



