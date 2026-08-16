 #Print a diamond pattern using stars (N = 4, i.e. 2N rows total):
N = 4

# Upper half
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(N - 1, 0, -1):
    for j in range(N - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
    
#output:

                  *
                 ***
                *****
               *******
                *****
                 ***
                  *
