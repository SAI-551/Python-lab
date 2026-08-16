# Print an inverted pyramid of stars (N = 5): 
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
#output:
    *********
     *******
      *****
       ***
        *
