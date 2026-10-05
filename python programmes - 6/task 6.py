import re
server_log = """
[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"
"""

# Named groups
pattern = re.compile(
    r"\[(?P<timestamp>[^\]]+)\]\s+"
    r"(?P<level>\w+)\s+"
    r"user=(?P<user>\w+)\s+"
    r'msg="(?P<msg>[^"]*)"'
)

# Parse log entries
entries = []

for match in pattern.finditer(server_log):
    entries.append(match.groupdict())

print("Log Entries:")
for entry in entries:
    print(entry)


# Count ERROR, WARN and INFO
error = 0
warn = 0
info = 0

for entry in entries:
    if entry["level"] == "ERROR":
        error += 1
    elif entry["level"] == "WARN":
        warn += 1
    elif entry["level"] == "INFO":
        info += 1

print("ERROR:", error)
print("WARN:", warn)
print("INFO:", info)


# Redact usernames
redacted = re.sub(
    r"user=\w+",
    "user=<hidden>",
    server_log
)

print("Redacted Log:")
print(redacted)


# Bonus - Sort by username and print ERROR entries
entries.sort(key=lambda x: x["user"])

print("ERROR entries:")

for entry in entries:
    if entry["level"] == "ERROR":
        print(entry["user"], "->", entry["msg"])
#output:
Log Entries:
{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
{'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}
{'timestamp': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}
ERROR: 1
WARN: 1
INFO: 1
Redacted Log:

[2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
[2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"

ERROR entries:
jsmith -> Disk quota exceeded
