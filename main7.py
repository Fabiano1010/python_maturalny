def opener(path):
    return open(path, "r").read().rstrip().splitlines()

file=opener("C:\\Users\\Home\\Desktop\\DANE\\liczby.txt")
file1=opener("C:\\Users\\Home\\Desktop\\DANE\\przyklad.txt")
def odbicie(file):
    return [int(i[::-1]) for i in file if int(i[::-1])%17==0]


print(odbicie(file))

def bezw(file):
    t=[abs(int(i)-int(i[::-1])) for i in file]
    return int(file[t.index(max(t))]), max(t)

print(bezw(file))

def czypierwsza(n):
    if n==2: return True
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

def znajdzpierwsze(file):
    return [(int(i)) for i in file if czypierwsza(int(i)) and czypierwsza(int(i[::-1]))]

print(znajdzpierwsze(file))

print(len(set(file)))

def powtarzajace(file):
    counter=0
    for i in file:
        if file.count(i)==2:
            counter+=1
    return int(counter/2)

print(powtarzajace(file))

def powtarzajace3(file):
    counter=0
    for i in file:
        if file.count(i)==3:
            counter+=1
    return int(counter/3)

print(powtarzajace3(file))

