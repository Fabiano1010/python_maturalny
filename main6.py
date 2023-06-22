def czypierwsza(n):
    if n <2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def sito(n):
    A = [True] * (n + 1)
    pierwsze=[]
    for i in range(2,n):
        if czypierwsza(i):
            pierwsze.append(i)
    for i in pierwsze:
        j=i*2
        while j<len(A):
            A[j]=False
            j+=i
    for i in range(2, len(A)):
        if A[i]:
            print(i,end=",")

n=20000
sito(n)

