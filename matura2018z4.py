path1="C:\\Users\\Home\\Desktop\\Dane_PR2\\przyklad.txt"
path2="C:\\Users\\Home\\Desktop\\Dane_PR2\\sygnaly.txt"
file1=open(path1,"r").read().rstrip().split('\n')
file2=open(path2,"r").read().rstrip().split('\n')

def zadanie1(file):
    sentence=''
    for i in range(39,len(file),40):
        sentence+=file[i][9]
    return sentence

print(zadanie1(file2))

def tablica(file):
    word=''
    t=[]
    for i in file:
        for j in i:
            if j not in word:
                word+=j
        t.append([word, len(word), file.index(i)])
        word=''
    return t

def zadanie2(file):
    rob=0
    ind=0
    t=tablica(file)
    for i in t:
        if i[1]>rob:
            rob=i[1]
            ind=i[2]


    result = file[ind] + " \n" + str(rob)
    return result

print(zadanie2(file2))

def order(word):
    t=[]
    for i in word:
        t.append(ord(i))
    maximum=max(t)
    minimum=min(t)
    if maximum-minimum<=10:
        return word
    else:
        pass
def zadanie3(file):
    t=[]
    for i in file:
        if order(i)!=None:
            t.append(order(i))
    return t

for i in zadanie3(file2):
    print(i)
