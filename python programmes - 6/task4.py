import re
pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

variables = ["_count2", "2fast", "total_sum"]

for variable in variables:
    if re.fullmatch(pattern, variable):
        print("Valid variable:", variable)
    else:
        print("Invalid variable:", variable)


# 2. cat, dog or bird
pets = "I have a cat, a dog and a bird. My cat likes the dog."

pattern = r"\b(cat|dog|bird)\b"

matches = re.findall(pattern, pets)
print("Pets:", matches)


# 3. Hexadecimal color codes
pattern = r"^#[A-Fa-f0-9]{3}([A-Fa-f0-9]{3})?$"

colors = ["#FFAA00", "#000", "#12FG45"]

for color in colors:
    if re.fullmatch(pattern, color):
        print("Valid color:", color)
    else:
        print("Invalid color:", color)


# 4. Named groups for log
log = "2024-06-01 08:15:32 ERROR Disk full"

pattern = (
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>\w+) "
    r"(?P<message>.*)"
)

match = re.search(pattern, log)

print("Date:", match.group("date"))
print("Time:", match.group("time"))
print("Level:", match.group("level"))
print("Message:", match.group("message"))
#output:
Valid variable: _count2
Invalid variable: 2fast
Valid variable: total_sum
Pets: ['cat', 'dog', 'bird', 'cat', 'dog']
Valid color: #FFAA00
Valid color: #000
Invalid color: #12FG45
Date: 2024-06-01
Time: 08:15:32
Level: ERROR
Message: Disk full
