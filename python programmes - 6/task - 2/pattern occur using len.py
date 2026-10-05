
# Count how many times the pattern occurs using len() on the result of findall()



import re

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r"\$\d+\.\d+", prices)

print(len(amounts))


#output:
#3
