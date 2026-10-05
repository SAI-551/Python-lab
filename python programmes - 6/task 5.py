import re
def is_valid_email(s):
    pattern = r"^[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$"
    return bool(re.fullmatch(pattern, s))


valid = [
    "john@gmail.com",
    "student@example.com",
    "test.user@yahoo.com",
    "abc123@college.in"
]

invalid = [
    "a@b.c",
    "no-at-sign.com",
    "user@gmail",
    "user@.com"
]

print("Valid Emails:")
for email in valid:
    print(email, is_valid_email(email))

print("Invalid Emails:")
for email in invalid:
    print(email, is_valid_email(email))


# 5.2 Phone Number Extractor

text = """
Call 555-123-4567 or (555) 123-4567.
You can also call 555.987.6543.
"""

pattern = r"(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}"

phones = re.findall(pattern, text)

print("Phone numbers:")

for phone in phones:
    number = re.sub(r"\D", "", phone)
    number = re.sub(
        r"(\d{3})(\d{3})(\d{4})",
        r"\1-\2-\3",
        number
    )
    print(number)


# 5.3 Date Extraction and Reformatting

text = "Dates are 12/06/2024 and 25/12/2024."

dates = re.findall(r"(\d{2})/(\d{2})/(\d{4})", text)

print("Extracted dates:", dates)

new_text = re.sub(
    r"(\d{2})/(\d{2})/(\d{4})",
    r"\3-\2-\1",
    text
)

print("ISO dates:", new_text)


# 5.4 Whitespace and HTML Cleanup

def clean_text(html):
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


html = """
<p>Hello   <b>World</b></p>
<p>Welcome to    Python.</p>
"""

print("Clean text:", clean_text(html))


# 5.5 Password Strength Checker

def check_password(pw):
    failed = []

    if len(pw) < 8:
        failed.append("At least 8 characters")

    if not re.search(r"[A-Z]", pw):
        failed.append("At least one uppercase letter")

    if not re.search(r"[a-z]", pw):
        failed.append("At least one lowercase letter")

    if not re.search(r"\d", pw):
        failed.append("At least one digit")

    if not re.search(r"[!@#$%^&*]", pw):
        failed.append("At least one symbol")

    return failed


passwords = [
    "Hello123!",
    "hello123",
    "HELLO123!",
    "HelloWorld!",
    "Hi1!"
]

for password in passwords:
    result = check_password(password)

    if len(result) == 0:
        print(password, "-> Strong")
    else:
        print(password, "-> Failed:", result)
#output:
Valid Emails:
john@gmail.com True
student@example.com True
test.user@yahoo.com True
abc123@college.in True
Invalid Emails:
a@b.c False
no-at-sign.com False
user@gmail False
user@.com False
Phone numbers:
555-123-4567
555-123-4567
555-987-6543
Extracted dates: [('12', '06', '2024'), ('25', '12', '2024')]
ISO dates: Dates are 2024-06-12 and 2024-12-25.
Clean text: Hello World Welcome to Python.
Hello123! -> Strong
hello123 -> Failed: ['At least one uppercase letter', 'At least one symbol']
HELLO123! -> Failed: ['At least one lowercase letter']
HelloWorld! -> Failed: ['At least one digit']
Hi1! -> Failed: ['At least 8 characters']
