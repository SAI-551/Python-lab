#A2.1:Write a program that:
#1.Stores your first name and last name in two separate string variables
first = "valuri"
last = "sai"
#2.Concatenates them into a full name with a space in between.
full_name = first + " " + last
#3.Prints the full name in UPPERCASE, lowercase, and Title Case.
print(full_name.upper())#VALLURI SAI
print(full_name.lower())#valluri sai
print(full_name.title())#Valluri sai
#4.Prints the length of the full name.
print(len(full_name))#10
#5.Prints the first character and the last character of the full name.
print(full_name[0], full_name[-1])#v i

#Task A2.2: Use string slicing to extract and print only your first name from the full name string 
full_name = "valluri sai"

first_name = full_name[:full_name.index(" ")]
print(first_name)#valluri
