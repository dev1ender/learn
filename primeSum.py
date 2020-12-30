import math
def isPrime(n):
    if(n<=1):
        return False
    if(n==2 or n == 3):
        return True
    if(n%2==0 or n%3==0):
        return False
    i=5
    while i*i < n:
        if(n%i==0 or n%(i+2)==0):
            return False
        i+=6
    return True

def primesum(A):
        hashMap = {}
        for i in range(1,int(math.sqrt(A))):
           
        print(hashMap)
        solutions = []
        for i in range(2,A):
            pass
            # i+=1
            # if(arr[i] and arr[A-i]):
            #     solutions.append(i)
            #     solutions.append(A-i)
            #     break
        return solutions

print(primesum(100))