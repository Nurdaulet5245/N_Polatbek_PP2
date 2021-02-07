def subtractProductAndSum(n: int) -> int:
    s = 0
    p = 1
    for i in str(n):
      s += int(i)
      p *= int(i)
    print(p - s)  

n = input()

subtractProductAndSum(n)