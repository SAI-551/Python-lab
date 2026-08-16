# Write a program to check whether a given number is a palindrome using a while loop.
num = int(input("Enter an integer: "))

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if num==reversed_num:
    print("palindrome")
else:
    print("not a palindrome")

#output:
    #Enter an integer: 143
    #not a palindrome

