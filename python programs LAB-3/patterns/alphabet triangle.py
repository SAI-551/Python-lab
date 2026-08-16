# Print the alphabet pattern below (N = 5, using uppercase letters):
N = 5

for i in range(N):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


    #output:
A 
B B 
C C C 
D D D D 
E E E E E 

