
#Print a hollow diamond pattern of stars (N = 4):

N = 4

# Upper half
for i in range(1, N + 1):
    print(" " * (N - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# Lower half
for i in range(N - 1, 0, -1):
    print(" " * (N - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
#output:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
