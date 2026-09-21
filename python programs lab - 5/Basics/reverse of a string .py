#2 Reverse a given string (without using slicing, then with slicing)


s = input("Enter a string: ")

reverse = ""
for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

print("Reversed string:", reverse)

#output:
#Enter a string: mani
#Reversed string: inam
#using slicing
str=s[::-1]
print("reversed string :",str)
#output:
#reversed string : inam


