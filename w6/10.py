n=int(input())
list = []
for i in range(0, n):
  el=int(input())
  list.append(el)

def uniq(list):
    x=[]
    for a in list:
        if a%2==0:
            x.append(a)
    return x
print(uniq(list))