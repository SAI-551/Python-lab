#2. Manipulation
#6 Count the occurrences of a specific character in a string.
python
s = input("Enter a string: ")
ch = input("Enter the character to count: ")

count = 0

for c in s:
    if c == ch:
        count += 1

print("Occurrences:", count)


