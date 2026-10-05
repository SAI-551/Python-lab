#Task 1: Basic Lambda Functions

### (a) Square of a number

square = lambda x: x * x

print("Square of 5:", square(5))


#**Output:**
#Square of 5: 25


### (b) Check if a number is even


is_even = lambda x: x % 2 == 0

print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))


#**Output:**


#Is 8 even? True
#Is 7 even? False


### (c) Find the larger of two numbers


larger = lambda a, b: a if a > b else b

print("Larger of 10 and 25:", larger(10, 25))


#**Output:**


#Larger of 10 and 25: 25

#Task 2: Lambda with Conditional Expression
 
grade = lambda marks: 'Pass' if marks >= 40 else 'Fail'

marks_list = [25, 40, 55, 32, 78, 90]

for marks in marks_list:
    print(marks, grade(marks))


    #output:
    #25 Fail
    #40 Pass
#55 Pass
#32 Fail
#78 Pass
#90 Pass


#Task 3: Sorting with Lambda as key
    
students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]
print("descending order:",sorted(students, key=lambda s: s[1], reverse=True))

#output:
#descending order: [('Sita', 92), ('Ravi', 78), ('Amit', 65)]

#Task 4: Lambda Inside map() and filter()
#  Given a list of numbers, use map() with a lambda to produce a list of their cubes.
numbers=[2,3,4,5,6]
cubes=list(map(lambda x:x*3,numbers))
print("cubes of the numbers in list:",cubes)

#output:
#cubes of the numbers in list: [6, 9, 12, 15, 18]

#•  Given the same list, use filter() with a lambda to extract only numbers divisible by 3.

numbers=[6,12,5,18,21]
divisors=list(filter(lambda x:x%3==0 ,numbers))
print("divisors of 3 in list:",divisors)

#output:
#divisors of 3 in list: [6, 12, 18, 21]


#Task 5: Lambda for Dictionary Value Sorting
 #Given a dictionary of item names mapped to prices, use sorted() with a lambda key to display the
#items from cheapest to most expensive

items = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5,
    "Bag": 500,
    "Eraser": 8
}

sorted_items = sorted(items.items(), key=lambda item: item[1])

for item, price in sorted_items:
    print(item, price)

    ##output:
    #Pencil 5
    #Eraser 8
    #Pen 10
    #Notebook 50
    #Bag 500






