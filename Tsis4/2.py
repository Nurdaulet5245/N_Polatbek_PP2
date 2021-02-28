import re

st=input()

for t in re.split(r",|\.", st):
    if t != '': print(t)