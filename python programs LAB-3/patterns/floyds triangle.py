#Print a floyd's triangle (N = 5 rows, consecutive natural numbers):
N = 5
num = 1

for i in range(1, N + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
