def czypierwsza(n):
    if n<2: return False
    if n==2: return True
    if n>2:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

print(czypierwsza(6))

def czynnik(n):
    k=2
    czynniki=[]
    while n>1:
        while n%k==0:
            czynniki.append(k)
            n=n/k
        k+=1
    return czynniki

print(czynnik(32))

def bubbles(t):
    for i in range(len(t)):
        for j in range(len(t)-i-1):
            if t[j]>t[j+1]:
                t[j+1], t[j] = t[j], t[j+1]
                # temp=t[j+1]
                # t[j+1]=t[j]
                # t[j]=temp

    return t

t=[2,5,7,1,2,5,6,9,123,34,10]


print(bubbles(t))
