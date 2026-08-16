#Exercise 4: Write a program to find the largest of three numbers using nested if-else.
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a>b and a>c:
    print("a is largest")
elif b>c and b>a:
    print("b is largest")
else:
    print("c is largest")
    #output:
#enter a value:8
#enter b value:5
#enter c value:9
#c is largest
