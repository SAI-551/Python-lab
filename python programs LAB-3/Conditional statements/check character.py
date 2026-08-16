ch=input("enter character:") 
if ch in "aeiouAEIOU":
    print("vowel")
elif ch.isalpha():
    print("consonant")
elif ch.isdigit():
    print("digit")
else:
    print("special character")

    #output:
    #enter character:a
    #vowel
    #enter character:p
    #consonant
    #enter character:7
    #digit
    #enter character:@
    #special character

    
