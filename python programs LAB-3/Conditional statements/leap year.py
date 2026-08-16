#Write a program to check whether a given year is a leap year or not.
n=int(input("enter year"))
if n%4==0:
    print("leap year")
elif n % 400==0:
    print("leap year")
elif n%100==0:
    print("not a leap year")
    
#output:
     #enter year 2024
     #leap year

    
