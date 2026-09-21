#3. Slicing & Indexing
#11 Extract the first and last characters of a string.

s = input("Enter a string: ")

print("First character:", s[0])
print("Last character:", s[-1])
#output:
#Enter a string: manikanta
#First character: m
#Last character: a


#12 Print every second character of a string.

s = input("Enter a string: ")

print("Every second character:", s[::2])
#output:
#Enter a string: manikanta
#Every second character: mnkna

#13 Check if a substring exists within a string.

s = input("Enter a string: ")
sub = input("Enter the substring to search: ")

if sub in s:
    print("Substring exists")
else:
    print("Substring does not exist")
    #output:
    #Enter a string: manikanta
#Enter the substring to search: mani
#Substring exists



#14 Find the index of the first and last occurrence of a character
   
s = input("Enter a string: ")
ch = input("Enter the character to search: ")

if ch in s:
    first = s.find(ch)
    last = s.rfind(ch)

    print("First occurrence index:", first)
    print("Last occurrence index:", last)
else:
    print("Character not found")
#output:
   # Enter a string: manikanta
#Enter the character to search: n
#First occurrence index: 2
#Last occurrence index: 6
