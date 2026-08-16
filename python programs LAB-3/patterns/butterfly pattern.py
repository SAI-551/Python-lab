# Print a butterfly pattern of stars (N = 4):
N = 4

# Upper half
for i in range(1, N + 1):
    print("*" * i, end="")
    print(" " * (2 * (N - i)), end="")
    print("*" * i)

# Lower half
for i in range(N - 1, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (N - i)), end="")
    print("*" * i)
#output:
*      *
**    **
***  ***
********
***  ***
**    **
*      *
