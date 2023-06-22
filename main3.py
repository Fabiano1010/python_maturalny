sentence="PENIS"
def sumascii(s):
    sum=0
    sum=[int(ord(i)) for i in s]
    sum=sum.
    if sum<2: return [False, sentence, sum]
    if sum==2:return [True, sentence, sum]
    for i in range(2,int(sum**0.5)+1):
        if sum%i==0:
            return [False, sentence, sum]
    return [True, sentence, sum]
print(sumascii(sentence))