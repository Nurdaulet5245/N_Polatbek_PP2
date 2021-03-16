def inRange(n, a, b):
    if int(n) in range(int(a), int(b)):
        print("in range")
    else :
        print("Out of range.")

n=input()
a=input()
b=input()
inRange(n, a, b)