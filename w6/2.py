n=int(input())
list = []
for i in range(0, n):
  el=int(input())
  list.append(el)
def sum(list):
    sum = 0
    for x in range(0, n):
        sum+=list[x]
    return sum
print(sum(list))