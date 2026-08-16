# Write a program to reverse a given integer using a while loop (e.g., 1234  4321). 
num = int(input("Enter an integer: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)
#output:
#Enter an integer: 123
#Reversed number = 321

