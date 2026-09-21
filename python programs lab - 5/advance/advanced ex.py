#5. Advanced
#20 Remove duplicate characters from a string.
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)
#output:
#Enter a string: manikanta
#After removing duplicates: manikt

#21 Check if a string contains only digits, only alphabets, or is alphanumeric.
s = input("Enter a string: ")

if s.isdigit():
    print("Only digits")
elif s.isalpha():
    print("Only alphabets")
elif s.isalnum():
    print("Alphanumeric")
else:
    print("Contains special characters or spaces")
    #output:
    #Enter a string: manikanta
#Only alphabets

#2 Find all the duplicate characters in a string and their counts.
    s = input("Enter a string: ")

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

print("Duplicate characters:")

for ch in count:
    if count[ch] > 1:
        print(ch, ":", count[ch])
        #output:
        #Enter a string: manikanta
        #Duplicate characters:
        #a : 3
        #n : 2

#23 Convert a string into a list of characters and back into a string.
        s = input("Enter a string: ")

# String to list
char_list = list(s)
print("List:", char_list)

# List back to string
new_string = "".join(char_list)
print("String:", new_string)
#output:
#Enter a string: maniikanta
#List: ['m', 'a', 'n', 'i', 'i', 'k', 'a', 'n', 't', 'a']
#String: maniikanta

#24 Write a program to check if a string is a valid identifier (like a Python variable name).
s = input("Enter an identifier: ")

if s.isidentifier():
    print("Valid identifier")
else:
    print("Invalid identifier")
    #output:
    #Enter an identifier: manikanta
    #Valid identifier

