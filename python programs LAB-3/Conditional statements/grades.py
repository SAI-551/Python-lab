#Exercise 5: Write a program that takes a student's marks and prints the grade using if-elif-else (A: 90, 
#B: 75–89, C: 60–74, D: 40–59, F: below 40).
marks=int(input("enter marks:"))
if marks>=90:
          print("grade A")
elif marks>=75 and marks<90:
          print("grade B")
elif marks>=60 and marks<75:
          print("grade C")
elif marks>=40 and marks<60:
          print("grade C")
else:
          print("fail")

#output:
          #enter marks:90
          #grade A
