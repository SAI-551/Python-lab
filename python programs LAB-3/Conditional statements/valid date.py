#Exercise 7: Write a program that accepts a year, month, and day, and determines whether the date is 
#valid, accounting for leap years and the number of days in each month.
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap_year = True
else:
    leap_year = False
days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
if leap_year:
    days_in_month[1] = 29
if month < 1 or month > 12:
    print("Invalid date")
elif day < 1 or day > days_in_month[month - 1]:
    print("Invalid date")
else:
    print("Valid date.")
    #output:
    #Enter year: 2007
    #Enter month (1-12): 5
    #Enter day: 20
    #Valid date.

