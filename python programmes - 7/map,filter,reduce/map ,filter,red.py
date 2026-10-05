#Task 1: Using map() to Transform Data
#•  Given a list of temperatures in Celsius, use map() with a named function (not a lambda) to convert
#them all to Fahrenheit.
#•  Given a list of strings, use map() to convert every string to uppercase.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperatures = [0, 10, 20, 30, 40]

fahrenheit = list(map(celsius_to_fahrenheit, temperatures))

print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)

#output:
Celsius: [0, 10, 20, 30, 40]
Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]

def to_uppercase(text):
    return text.upper()

words = ["hello", "python", "programming", "world"]

uppercase_words = list(map(to_uppercase, words))

print(uppercase_words)
#output:['HELLO', 'PYTHON', 'PROGRAMMING', 'WORLD']


#Task 2: Using filter() to Select Data
#•  Given a list of integers from 1 to 50, use filter() to extract all prime numbers (write a helper function
#is_prime()).
#•  Given a list of words, use filter() to keep only palindromes.
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


numbers = list(range(1, 51))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)


#output:Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def is_palindrome(word):
    return word == word[::-1]


words = ["madam", "hello", "level", "python", "radar", "world", "civic"]

palindromes = list(filter(is_palindrome, words))

print("Palindromes:", palindromes)
#output:Palindromes: ['madam', 'level', 'radar', 'civic']


#Task 3: Using reduce() to Aggregate Data
#•  Import reduce from functools. Given a list of numbers, use reduce() to compute: (a) their product,
#(b) the maximum value, without using the built-in max() function.
#•  Use reduce() to concatenate a list of strings into a single sentence.

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)
#output:Product: 120

from functools import reduce

numbers = [12, 45, 7, 89, 23, 56]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum:", maximum)
#output:Maximum: 89

from functools import reduce

words = ["Python", "is", "a", "powerful", "language"]

sentence = reduce(lambda a, b: a + " " + b, words)

print(sentence)

#output:Python is a powerful language


#Task 4: Chaining map(), filter() and reduce()
#•  Given a list of numbers, write a single pipeline that: (1) filters out the odd numbers, (2) maps the
#remaining even numbers to their squares, and (3) reduces the squared values to their total sum.
#•  Solve the same problem again using a single list comprehension and sum(), and compare
#readability with your notes.
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x ** 2, evens)
total = reduce(lambda a, b: a + b, squares)

print("Total:", total)
#output:Total: 220

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = sum(x ** 2 for x in nums if x % 2 == 0)

print("Total:", total)
#output:Total: 220


#Task 5: Employee Records Processing
#•  Given a list of dictionaries, each representing an employee with keys 'name', 'department' and
'salary':
#•  - Use filter() to select employees from a specific department.
##•  - Use map() to give every selected employee a 10% salary hike (return new dictionaries; do not
#mutate the originals).
#•  - Use reduce() to compute the total salary expenditure for that department after the hike

    from functools import reduce

employees = [
    {"name": "Alice", "department": "IT", "salary": 50000},
    {"name": "Bob", "department": "HR", "salary": 45000},
    {"name": "Charlie", "department": "IT", "salary": 60000},
    {"name": "David", "department": "Finance", "salary": 55000},
    {"name": "Eva", "department": "IT", "salary": 70000}
]

# Select employees from the IT department
it_employees = filter(
    lambda employee: employee["department"] == "IT",
    employees
)

# Give selected employees a 10% salary hike
hiked_employees = map(
    lambda employee: {
        **employee,
        "salary": employee["salary"] * 1.10
    },
    it_employees
)

# Convert the map result to a list
hiked_employees = list(hiked_employees)

# Calculate total salary expenditure
total_salary = reduce(
    lambda total, employee: total + employee["salary"],
    hiked_employees,
    0
)

print("Employees after 10% hike:")

for employee in hiked_employees:
    print(employee)

print("Total salary expenditure:", total_salary)

#output:
Employees after 10% hike:
{'name': 'Alice', 'department': 'IT', 'salary': 55000.00000000001}
{'name': 'Charlie', 'department': 'IT', 'salary': 66000.0}
{'name': 'Eva', 'department': 'IT', 'salary': 77000.0}

Total salary expenditure: 198000.0
