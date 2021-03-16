def max_2(a, b):
    if int(a)>int(b):
        return int(a)
    else:
        return int(b)
def max_3(a, b, c):
	return max_2(c, max_2(a, b))

a=input()
b=input()
c=input()
print(max_3(a, b, c))
