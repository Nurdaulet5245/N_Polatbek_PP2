def largestAltitude(gain: []) -> int:
    altitudes = [0]
    for i in gain:
      altitudes.append(altitudes[-1] + i)
    print(max(altitudes))

n=int(input())
l = []
for i in range(0, n):
  el=int(input())
  l.append(el)

largestAltitude(l)