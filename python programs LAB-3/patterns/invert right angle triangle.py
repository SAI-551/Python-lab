#Print an inverted right-angled triangle of stars (N = 5):


for i in range(5, 0, -1):
    for j in range(i):
        print(" * ", end="")
    print()

#output:
    *  *  *  *  * 
    *  *  *  * 
    *  *  * 
    *  * 
    * 
