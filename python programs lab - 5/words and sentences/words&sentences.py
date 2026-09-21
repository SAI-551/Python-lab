#4. Words & Sentences
#15 Count the number of words in a sentence.

s = input("Enter a sentence: ")

words = s.split()

print("Number of words:", len(words))
#output:
#Enter a sentence: mani ram abhi
#Number of words: 3



#16 Find the longest word in a sentence.

s = input("Enter a sentence: ")

words = s.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
#output:
#Enter a sentence: manikanata abhi ram
#Longest word: manikanata


#17 Reverse the order of words in a sentence (without reversing each word).

s = input("Enter a sentence: ")

words = s.split()
words.reverse()

result = " ".join(words)

print("Reversed sentence:", result)
#output:
#Enter a sentence: i love python
#Reversed sentence: python love i

#18 Capitalize the first letter of every word (Title Case), without using .title().

s = input("Enter a sentence: ")

words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print("Title Case:", result.strip())
#output:
#Enter a sentence: manikanta is good boy
#Title Case: Manikanta Is Good Boy

#19 Check if two strings are anagrams of each other

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
#output:
    #Enter first string: mani
#Enter second string: kanta
#The strings are not anagrams

