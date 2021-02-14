n=int(input())
l = []
for i in range(0, n):
  el=int(input())
  l.append(el)

for x in range(0, n):
    if l[x]%2==0 :
        print(l[x])


