# Write a program to find the sum and average of digits of a given number using a while loop.
num = int(input("Enter a number: "))

n = abs(num)
sum_digits = 0
count = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    count += 1
    n //= 10

if count > 0:
    average = sum_digits / count
else:
    average = 0

print("Sum of digits =", sum_digits)
print("Average of digits =", average)
#output:
#Enter a number: 1234
#sum of digits = 10
#Average of digits = 2.5

s
