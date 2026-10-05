#TASK 1     Basic Pattern Matching

# Given sentence = "1024 requests were served in 3 seconds", use re.match() to test
#whether the sentence starts with a digit

import re

sentence="1024 requests were served in 3 seconds"

result=re.match(r"^\d",sentence)

if result:
    print("sentence start with a digit")
else:
    print("sentence does not start with a digit")

#output:
    #sentence start with a digit

