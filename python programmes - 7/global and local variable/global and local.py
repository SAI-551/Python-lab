#Task 1: Local vs Global Scope
#•  Declare a global variable counter = 0 at the top of the program.
#•  Write a function show_local() that creates a local variable with the same name and prints it, then
#print the global variable outside the function.
#•  Explain in your record why the two values are different

counter=0
def show_local():
    counter=10
    print("local variable:",counter)
show_local()

print("global variable:",counter)

#output:
#local variable: 10
#global variable: 0


#Task 2: Modifying a Global Variable Using the global Keyword
#•  Write a function increment_counter() that uses the global keyword to modify the global counter
#variable defined in Task 1, incrementing it by 1 each time it is called.
#•  Call the function 5 times and print the counter value after each call


counter = 0

def increment_counter():
    global counter
    counter += 1

for i in range(5):
    increment_counter()
    print("Counter:", counter)

#output:

#Counter: 1
#Counter: 2
#Counter: 3
#Counter: 4
#Counter: 5

#Task 3: UnboundLocalError Demonstration
#•  Write a function that tries to modify a global variable inside it without declaring it global, and
#observe/record the UnboundLocalError that Python raises.
#•  Fix the function using the global keyword and show that it now works correctly

count = 10

def increase_count():
    count += 1
    return count

try:
    print(increase_count())
except UnboundLocalError as e:
    print("Error:", e)

def increase_count_fixed():
    global count
    count += 1
    return count

print("After fixing:", increase_count_fixed())

#output:
#Error: cannot access local variable 'count' where it is not associated with a value
#After fixing: 11

#Task 4: Nested Functions and the nonlocal Keyword
#•  Write an outer function make_counter() that defines a local variable count = 0 and an inner
#function increment() that increases count using the nonlocal keyword.
#•  Have make_counter() return the inner function, then call it multiple

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


# Create a counter
counter = make_counter()

# Call the counter multiple times
print(counter())
print(counter())
print(counter())
print(counter())

#output:
#1
#2
#3
#4

#Task 5: Bank Account Simulation (Applied Scope Exercise)
#•  Write a program that maintains a global variable balance = 1000.
#•  Write functions deposit(amount) and withdraw(amount) that correctly update the global balance
#using the global keyword, with withdraw() also checking for insufficient funds.
#•  Write a menu-driven loop that lets the user deposit, withdraw, or check the balance until they
#choose to exit

balance = 1000


def deposit(amount):
    global balance
    balance += amount
    print(f"₹{amount} deposited successfully.")


def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")


def check_balance():
    print(f"Current balance: ₹{balance}")


# Menu-driven loop
while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you for using the bank account system.")
        break

    else:
        print("Invalid choice. Please try again.")


#output:
        #--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current balance: ₹1000

Enter your choice: 1
Enter deposit amount: 500
₹500 deposited successfully.

Enter your choice: 2
Enter withdrawal amount: 200
₹200 withdrawn successfully.

Enter your choice: 3
Current balance: ₹1300

Enter your choice: 4
Thank you for using the bank account system.



    
