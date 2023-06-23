import math

path="C:\\Users\\Home\\Downloads\\Dane_NOWA\\punkty.txt"
path2=""

file = open(path, "r").read().rstrip().split('\n')
t=[]
for i in file:
    t.append(i.split())

def punkty(t):
    x,y=200,200
    r=200
    brzeg=[]
    wew=[]
    zew=[]

    for i in t:
        fun=(((x-int(i[0]))**2)+((y-int(i[1]))**2))
        if fun>r**2:
            zew.append(i)
        elif fun==r**2:
            brzeg.append(i)
        elif fun<r**2:
            wew.append(i)

    return (len(wew)), brzeg

# print(punkty(t))

def pisearch(t, iteration):
    x, y = 200, 200
    r = 200
    k=[]
    pkw=400*400
    # pko=200**2*
    for i in range(iteration):
        fun = (((x - int(t[i][0])) ** 2) + ((y - int(t[i][1])) ** 2))
        if fun < r ** 2 or fun == r ** 2:
            k.append(i)
    pko=(len(k)/iteration)*pkw
    pi=pko/r**2
    return round(pi,4)
# print(pisearch(t,100))
# print(pisearch(t,1000))
# print(pisearch(t,5000))
# print(pisearch(t,len(t)))


def bladbez(t, iteration):
    ta=[]
    for i in range(1,iteration+1):
        pi=(pisearch(t, i))
        ta.append([round(abs(math.pi-pi),4), i])
    return ta

x=bladbez(t,1700)
sr=""
for i in x:
    sr+=str(i[0])+"\t"+str(i[1])+"\n"

file2=open("wynik.txt", "w")
file2.write(sr)
