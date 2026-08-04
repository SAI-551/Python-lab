#B4. Logical Operators
#Operators: and , or , not
#Task B4.1: A student is eligible for a scholarship if their percentage is above 75 AND attendance is
#above 90%. Write a program that takes percentage and attendance as input and prints whether the
#student is eligible, using logical operators.
percentage = float(input("enter percentage:"))#enter percentage:80
attendance = float(input("enter attendace %:"))#enter attendance:95
eligible = percentage > 75 and attendance > 90 
print("eligible for scholarship:",eligible)#eligible for scholarship:True
