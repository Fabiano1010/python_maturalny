path="C:\\Users\\Home\\Downloads\\Dane_PR2\\pary.txt"
path2="C:\\Users\\Home\\Downloads\\Dane_PR2\\przyklad.txt"
file= open(path2, "r").read().rstrip().split("\n")

def tablica(file):
    t=[]
    temp1=[]
    temp2=[]
    x=''
    y=''
    for i in file:
        for j in i:
            if 49<=ord(j)<=57:
                x+=j
            if 97<=ord(j)<=122:
                y+=j

        temp1.append(int(x))
        temp2.append(y)
        x,y='',''
    for i in range(len(temp1)):
        t.append([temp1[i],temp2[i]])
    return t, temp1, temp2

t=tablica(file)[0]
liczby=tablica(file)[1]
slowa=tablica(file)[2]

def pierwsze(n):
    k=2
    for i in range(2, int(n**0.5)+1):
        if n%k==0:
            return
        k+=1
    return n


def gold(n):
    prime = [pierwsze(i) for i in range(2, n) if pierwsze(i) != None]
    if n > 4 and n % 2 == 0:
        for i in prime:
            for j in prime:
                if i + j == n:
                    return [n,i,j]


def zadanie41(liczby):
    t=[]
    for i in liczby:
        if gold(i)!=None:
            t.append(gold(i))
    return t
z=zadanie41(liczby)
# for i in z:
#     print(i[0], i[1], i[2])

def ciag(slowa):
    t=[]
    for i in slowa:
        counter=1
        maxi=1
        l=''
        for j in range(len(i)):
            if ord(i[j-1])==ord(i[j]):
                counter+=1
                if counter>maxi:
                    maxi=counter
                    l=i[j]
            else:
                counter=1
        if l=='':
            t.append([i,i[0], maxi])
        else:
            t.append([i, l * maxi, maxi])
    return t
c=ciag(slowa)
# for i in c:
#     print(i[2], i[1])

def para(liczby, slowa):
    t=[]
    mini=0
    word=''
    for i in range(len(liczby)):
        if liczby[i]==len(slowa[i]):
            t.append([liczby[i],slowa[i]])
    for i in range(len(t)):
        if t[i-1][0]<t[i][0]:
            mini=t[i-1][0]
            word=t[i-1][1]
        if t[i-1][0]==t[i][0]:
            if t[i-1][1]<t[i][1]:
                mini = t[i - 1][0]
                word = t[i - 1][1]
    return mini, word

print(para(liczby, slowa))



