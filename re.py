import re

pattern = "abc"
text = "123 abc abc 456"

match = re.match(pattern, text)

if match:
    print("Found")
else:
    print("Not Found")