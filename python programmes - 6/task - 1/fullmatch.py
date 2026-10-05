# Use re.fullmatch() to check whether the string "12345" consists only of digits, then test it again
#on "123a5".



import re


result=re.fullmatch(r"\d+","12345")
print(result)
result1=re.fullmatch(r"\d+","123a5")
print(result1)


#output:
#<re.Match object; span=(0, 5), match='12345'>
#None


# In one or two sentences, explain in a comment why match() and fullmatch() gave different results
#for the same pattern on a string that starts with digits but contains other characters later





# match() only checks from the beginning, while fullmatch() requires the entire
# string to match the pattern, so later non-digit characters cause fullmatch() to fail.
