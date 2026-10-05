#LAB 1: Defining and Calling Functions
#Task 1: Simple Greeting Function
#•  Define a function greet() that takes a name as a parameter and prints "Hello, ! Welcome to
#Python."
#•  Call the function with at least 3 different names

def greet(name):
    print(f"Hello,{name} !welcome to python")
greet("mani")
greet("ram")
greet("abhi")
#output:
#Hello,mani !welcome to python
#Hello,ram !welcome to python
#Hello,abhi !welcome to python

#Task 2: Simple Interest Calculator
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)

simple_interest(5000, 5, 2)
#output:Simple Interest = 500.0

#Task 3: Even or Odd Checker

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check_even_odd(10)
#output:10 is Even


#Task 4: Function Returning Multiple Values
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication

sum_result, difference, product = calculate(10, 5)

print("Addition:", sum_result)
print("Subtraction:", difference)
print("Multiplication:", product)

#output:Addition: 15
#Subtraction: 5
#Multiplication: 50

#Task 5: Temperature Converter (Nested Function Calls
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def temperature_converter(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit_to_celsius(fahrenheit)

result = temperature_converter(25)

print("Celsius:", 25)
print("Converted back to Celsius:", result)

#0utput:
#Celsius: 25
#Converted back to Celsius: 25.0






