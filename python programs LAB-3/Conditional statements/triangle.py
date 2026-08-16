#Write a program that accepts three sides of a triangle and determines whether it is
#equilateral, isosceles, scalene, or not a valid triangle at all
a=int(input("enter one side:"))
b=int(input("enteer second side:"))
c=int(input("enter third side:"))
if a+b<c:
    print("not a valid triangle")

if a==b==c:
    print("equilateral triangle")
elif a==b!=c:
    print("isosceless triangle")
else:
    print("scalane triangle")
    #output:
    #enter one side:4
    #enteer second side:4
     #enter third side:4
    #  equilateral triangle

