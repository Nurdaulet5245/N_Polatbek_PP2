n=int(input())
l = []
for i in range(0, n):
  el=int(input())
  l.append(el)

for x in range(1, n):
    if l[x]>0 and l[x-1]>0 :
        print(l[x-1])
        print(l[x])
        break
    elif l[x]<0 and l[x-1]<0:
        print(l[x-1])
        print(l[x])
        break

