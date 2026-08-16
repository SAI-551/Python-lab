# Write a program to count the number of vowels, consonants, digits, and spaces in a given 
#string.
text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
#output:
#Enter a string: mani
#Vowels = 2
#Consonants = 2
#digits = 0
#Spaces = 0

