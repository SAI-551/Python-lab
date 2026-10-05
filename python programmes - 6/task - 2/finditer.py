# Use re.finditer() on the same paragraph to find every word longer than 6 characters, and print
#each match together with its start index.
import re

paragraph = "NASA and USA worked together with the United Nations and ISRO."

for match in re.finditer(r"\b\w{7,}\b", paragraph):
    print(match.group(), match.start())



#output:
    #together 20
    #Nations 45
