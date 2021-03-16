n=int(input())
list = []
for i in range(0, n):
  el=int(input())
  list.append(el)
def sum(list):
    mul = 1
    for x in range(0, n):
        mul*=list[x]
    return mul
print(sum(list))