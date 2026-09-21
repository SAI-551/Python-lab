# Use a list comprehension to create a list of all even numbers between 1 and 50

list=[n for n in range(1,51) if n%2==0]
print("even numbers 1 to 50:",list)


#output:
#even numbers 1 to 50: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
