#Write a program to check whether a given number is prime using a for loop.
num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

        #output:
        Enter a number: 9
        Not a prime number

