import re
# Task 3

import re

text = "vanjarapumani@gmail.com or admin@example.com for help."

hidden = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "[EMAIL HIDDEN]", text)
print("Hidden emails:", hidden)

name = "Doe, John"

converted = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", name)
print("Converted name:", converted)

sentence = "I have 3 apples and 5 oranges."

def double_number(match):
    return str(int(match.group()) * 2)

doubled = re.sub(r"\d+", double_number, sentence)
print("Doubled numbers:", doubled)

text = "Wait!!! What??? Really!!!"

result, count = re.subn(r"([!?])\1+", r"\1", text)
print("After replacement:", result)
print("Number of replacements:", count)
#output:
Hidden emails: Contact [EMAIL HIDDEN] or [EMAIL HIDDEN] for help.
Converted name: John Doe
Doubled numbers: I have 6 apples and 10 oranges.
After replacement: Wait! What? Really!
Number of replacements: 3
