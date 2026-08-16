#Write a program to print all prime numbers between two given limits. 

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
#output:
        Enter the lower limit: 3
Enter the upper limit: 15
Prime numbers between 3 and 15 are:
3 5 7 11 13 
