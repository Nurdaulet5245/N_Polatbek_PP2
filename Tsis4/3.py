import re
s = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(s.group(1) if s else -1)