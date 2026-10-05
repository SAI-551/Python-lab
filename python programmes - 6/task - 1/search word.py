#Use re.search() to find the word "served" anywhere in the sentence and print its start/end
#position with .span()

import  re

sentence= "1024 requests were served in 3 seconds"

result=re.search(r"served",sentence)

if result:
    print("start and end position:",result.span())


#output:
    #start and end position: (19, 25)

    
