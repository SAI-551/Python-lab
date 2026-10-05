#LAB 2: Types of Function Arguments
#Task 1: Positional and Keyword Arguments

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)
print("Positional Arguments:")
student_info("Rahul", 101, "CSE")

print("Keyword Arguments:")
student_info(branch="CSE", name="Rahul", roll_no=101)

#output:
#Positional Arguments:
#Name: Rahul
#Roll No: 101
#Branch: CSE
#Keyword Arguments:
#Name: Rahul
#Roll No: 101
#Branch: CSE

#Task 2: Default Arguments

def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price

print("Price with default tax and discount:",
      calculate_price(1000))

print("Price with custom tax rate:",
      calculate_price(1000, 10))

print("Price with custom tax and discount:",
      calculate_price(1000, 12, 100))
#output:
#Price with default tax and discount: 1180.0
#Price with custom tax rate: 1100.0
#Price with custom tax and discount: 1020.0


#Task 3: Variable-Length Arguments (*args)
def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

total, average = total_marks(80, 75, 90)
print("3 Marks -> Total:", total, "Average:", average)

total, average = total_marks(85, 78, 92, 88, 95)
print("5 Marks -> Total:", total, "Average:", average)

total, average = total_marks(95)
print("1 Mark -> Total:", total, "Average:", average)

#Output:

#3 Marks -> Total: 245 Average: 81.66666666666667
#5 Marks -> Total: 438 Average: 87.6
#1 Mark -> Total: 95 Average: 95.0


#Task 4: Keyword Variable-Length Arguments (**kwargs)
def build_profile(**details):
    print("PROFILE CARD")

    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")


build_profile(
    name="Rahul",
    age=20,
    city="Hyderabad",
    hobby="Coding"
)

build_profile(
    name="Priya",
    city="Warangal",
    hobby="Reading",
    course="B.Tech"
)
#Output:
#PROFILE CARD
#Name: Rahul
#Age: 20
#City: Hyderabad
#Hobby: Coding

#PROFILE CARD
#Name: Priya
#City: Warangal
#Hobby: Reading
#Course: B.Tech


#Task 5: Combining All Argument Types
def order_summary(customer, *items, discount=0, **extra):
   
    print("Customer:", customer)

    print("\nOrdered Items:")
    for item in items:
        print("-", item)

    print("\nDiscount:", discount, "%")

    if extra:
        print("\nExtra Information:")
        for key, value in extra.items():
            print(f"{key.replace('_', ' ').title()}: {value}")


order_summary(
    "Rahul",
    "Laptop",
    "Wireless Mouse",
    "Keyboard",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)

#Output:Customer:
#Rahul
#Ordered Items:
#- Laptop
#- Wireless Mouse
#- Keyboard

#Discount: 10 %

#Extra Information:
#Delivery Address: Hyderabad
#Gift Wrap: True









