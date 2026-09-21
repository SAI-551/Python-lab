# Count the number of vowels, consonants, digits, and spaces in a string
s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
#output:
#Enter a string: manikanta
#Vowels: 4
#Consonants: 5
#Digits: 0
#Spaces: 0
