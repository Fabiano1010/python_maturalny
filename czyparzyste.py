path="C:\\Users\\Home\\Desktop\\liczby.txt"
file=open(path, "r").read().rstrip().split('\n')

def czyparz(licz):
    if licz%2==0:
        return True

def zbierz(file):
    t=[]
    num=''
    for i in file:
        if czyparz(int(i[-2])) and not czyparz(int(i[2])):
            num=i[-2]+i[2]

            t.append((int(num)))
        num=''

    return t

def zadanie(file):
    liczby=zbierz(file)
    counter=0
    for i in range(len(liczby)-1):
        if liczby[i]-liczby[i+1]<0:
            counter+=1

    return counter


print(zadanie(file))


print((zbierz(file)))

