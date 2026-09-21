#Remove all whitespace from a string

s = input("Enter a string: ")

result = ""

for ch in s:
    if not ch.isspace():
        result += ch

print("String without whitespace:", result)

#OUTPUT:
#Enter a string: MA  NI KAN TA
#String without whitespace: MANIKANTA

