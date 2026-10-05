 #TASK 2  |  Finding All Matches

# Given a paragraph of text, use re.findall() to extract every word that is written in all capital letters
#(e.g. "NASA", "USA")

import re

paragraph = "NASA and USA worked together with the United Nations and ISRO."

capital_words = re.findall(r"\b[A-Z]+\b", paragraph)

print("capital words in the paragraph:",capital_words)


#output:
#capital words in the paragraph: ['NASA', 'USA', 'ISRO']

