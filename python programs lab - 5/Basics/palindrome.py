#Check if a given string is a palindrome.

str=input("enter a string:")
s=str[::-1]
if s==str:
    print("palindrome")
else:
    print("not a palindrome")
    #output:
    #enter a string:mam
#palindrome

