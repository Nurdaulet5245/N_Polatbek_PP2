def isPrime(n):
    if (int(n)==1):
        return False
    elif (int(n)==2):
        return True;
    else:
        for x in range(2,int(n)):
            if(int(n) % x==0):
                return False
        return True
n=input()             
print(isPrime(n))