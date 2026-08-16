# Print a number triangle where each row repeats its row number (N = 5):
N = 5

for i in range(1, N + 1):
    for j in range(i):
        print(i, end=" ")
    print()

#output:

                    1 
                    2 2 
                    3 3 3 
                    4 4 4 4 
                    5 5 5 5 5 
