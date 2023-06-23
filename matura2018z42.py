path="C:\\Users\\Home\\Downloads\\Dane_PR\\sygnaly.txt"
path2="C:\\Users\\Home\\Downloads\\Dane_PR\\przyklad.txt"
file=open(path, "r").read().rstrip().split('\n')

def przekaz(t):
    word=''
    for i in range(39,len(t),40):
        word+=t[i][9]

    return word

print(przekaz(file))
#
# pliczek=open("wynik1.txt", "w")
# pliczek.write(przekaz(file))

def litery(t):
    words=[]

    for i in t:
        words.append(len(list(set(list(i)))))

    maxi=max(words)

    return t[words.index(maxi)], maxi

print(litery(file))

def distance(strg):
    s=[ord(i) for i in strg]
    t=[]
    for i in range(len(s)):
        for j in range(1,len(s)):
            temp=abs(s[i]-s[j])
            t.append(temp)
    if max(t)<=10:
        return strg
    return

def zadanie43(t):
    temp=[distance(i) for i in t if distance(i)!=None]
    return temp
x= zadanie43(file)
for i in range(len(x)):
    print(x[i])
