# Task 1: Factorial Using Recursion

### Recursive version

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))

#output:
#Factorial of 5: 120
#Factorial of 0: 1
#Factorial of -3: Factorial is not defined for negative numbers

#Iterative version
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print("Factorial of 5:", factorial_iterative(5))

#output:Factorial of 5: 120

#Difference

#The recursive version calls itself with n - 1 until it reaches the base case. The iterative version uses a for loop and does not make recursive function calls.


#Task 2: Fibonacci Series Using Recursion
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("First 15 Fibonacci terms:")

for i in range(15):
    print(fibonacci(i), end=" ")

#Output:

#First 15 Fibonacci terms:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


#Task 3: Sum of Digits and Digit Reversal
Sum of digits
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)


print("Sum of digits of 12345:", sum_of_digits(12345))

#Output:
#Sum of digits of 12345: 15

#Reverse a number recursively
def reverse_number(n, result=0):
    if n == 0:
        return result

    return reverse_number(n // 10, result * 10 + n % 10)


print("Reverse of 12345:", reverse_number(12345))
print("Reverse of 908:", reverse_number(908))

#Output:

#Reverse of 12345: 54321
#Reverse of 908: 809


#Task 4: Power Function Using Recursion
def power(base, exp):
    # Base case
    if exp == 0:
        return 1

    # Negative exponent
    if exp < 0:
        return 1 / power(base, -exp)

    # Recursive case
    return base * power(base, exp - 1)


print("2^5 =", power(2, 5))
print("5^0 =", power(5, 0))
print("2^-3 =", power(2, -3))

#Output:

#2^5 = 32
#5^0 = 1
#2^-3 = 0.125



#Task 5: GCD Using Recursion


def gcd(a, b):
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


print("GCD of 48 and 18:", gcd(48, 18))
print("LCM of 48 and 18:", lcm(48, 18))

#Output:

#GCD of 48 and 18: 6
#LCM of 48 and 18: 144




#Task 6: Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination)


print("Tower of Hanoi for 3 disks:")
tower_of_hanoi(3, "A", "B", "C")

print("\nTower of Hanoi for 4 disks:")
tower_of_hanoi(4, "A", "B", "C")
#Output for 3 disks:
#Tower of Hanoi for 3 disks:
#Move disk 1 from A to C
#Move disk 2 from A to B
#Move disk 1 from C to B
#Move disk 3 from A to C
#Move disk 1 from B to A
#Move disk 2 from B to C
#Move disk 1 from A to C


