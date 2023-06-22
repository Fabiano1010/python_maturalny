path = "C:\\Users\\Home\\Downloads\\Dane_2205\\liczby.txt"
path2="C:\\Users\\Home\\Downloads\\Dane_2205\\przyklad.txt"
file=open(path, "r").read().rstrip().split("\n")

def zad1(file):
    x = [[i[0]+i[-1],i] for i in file if i[0]==i[-1]]
    return len(x),x[0]

# print(zad1(file))
def czynniki(n):
    t=[]
    for k in range(2,int(n**0.5)+1):
        while n%k==0:
            n=n//k
            t.append(k)
            if n==1:
                break
    return t


def zad2(file):
    t=[]
    t2=[]
    t3=[]
    for i in file:
        i=int(i)
        t.append(czynniki(i))
    for i in t:
        t2.append(len(i))

    for i in t:
        t3.append(len(set(i)))


    return max(t2), t[t2.index(max(t2))], file[t2.index(max(t2))], max(t3), file[t3.index(max(t3))]

# print(zad2(file))

file2 = [int(i) for i in file]


def zad3a(file):
    t=[]
    for i in file:
        for j in file:
            if j!=i and j%i==0:
                for k in file:
                    if k!=j and k%j==0:
                        t.append([i,j,k])
    return len(t),t

def zad3b(file):
    t=[]
    for i in file:
        for j in file:
            if j!=i and j%i==0:
                for k in file:
                    if k!=j and k%j==0:
                        for l in file:
                            if l != k and l % k == 0:
                                for m in file:
                                    if m != l and m % l == 0:
                                        t.append([i,j,k,l,m])
    return len(t),t

print(zad3a(file2))

print(zad3b(file2))
# print(file2)