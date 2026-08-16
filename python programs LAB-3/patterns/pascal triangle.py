#Print Pascal's-Triangle-style pattern using increasing then decreasing numbers (N = 5):
N = 5

for i in range(1, N + 1):
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

    #output:
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

