# Write a program to generate the Fibonacci series up to N terms using a while loop. 
n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1


    #output:
    #Enter the number of terms: 5
    #0 1 1 2 3 

