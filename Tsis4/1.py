import re

n = input()
pattern = r'^[-+]?[0-9]*\.[0-9]+$'
for i in range(0, int(n)):
  st = input()
  if(re.search(pattern, st)):
  	print("valid")
  else:
  	print("invalid")