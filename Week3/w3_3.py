n=int(input())
pos = 0
l = []
for i in range(0, n):
  el=int(input())
  l.append(el)

for x in range(0, n):
    if l[x]>0 :
        pos+=1

print(pos)
