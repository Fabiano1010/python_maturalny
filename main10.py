path="C:\\Users\\Home\\Downloads\\DANE_2105\\instrukcje.txt"
path2="C:\\Users\\Home\\Downloads\\DANE_2105\\przyklad.txt"
file= open(path, "r").read().rstrip().split("\n")
t=[]
for i in file:
   t.append([i[0:-2:1], i[-1]])

def napis(t):
    napis=[]
    for i in t:
        if i[0]=="DOPISZ":
            napis.append(i[1])
        if i[0] =="ZMIEN":
            napis[-1]=i[1]
        if i[0]=="USUN":
            for j in range(int(i[1])):
                napis.pop()
        if i[0]=="PRZESUN":
            for j in range(len(napis)):
                if napis[j]==i[1]:
                    if ord(napis[j])<ord("Z"):
                        napis[j]=chr(ord(i[1])+1)
                        break
                    if ord(napis[j])==ord("Z"):
                        napis[j]="A"
                        break
    return "".join(napis)
napis=napis(t)

print("Zadanie 4.1:")
print("Długość napisu to {}".format(len(napis))+" znaków")

def ciag(t):
    counter = 1
    maxi=1
    inst=''
    for i in range(0,len(t)):
        if t[i-1][0]==t[i][0]:
            counter+=1
            if counter>maxi:
                maxi=counter
                inst=t[i][0]
        else:
            counter=1
    return maxi, inst
print("Zadanie 4.2:")
print("Najczęście występuje instrukcja: {}, {} razy".format(ciag(t)[1],ciag(t)[0]))

def powlitera(t):
    letters=[]
    maximum = 0
    l=''
    for i in t:
        if i[0]=="DOPISZ":
            letters.append(i[1])
    for i in letters:
        counter = letters.count(i)
        if counter > maximum:
            maximum = counter
            l=i

    return maximum, l
print("Zadanie 4.3:")
print("Najczęściej występującą literą w instrukcji DOPISZ jest {}, występuje {} razy".format(powlitera(t)[1],powlitera(t)[0]))

print("Zadanie 4.4:\nWyraz to:")
print(napis)