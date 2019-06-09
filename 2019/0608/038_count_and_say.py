def countAndSay(n):
    seq="1"
    for i in xrange(n-1):
        seq=getNext(seq)
    return seq
def getNext(seq):
    i, next_seq=0,""
    while i < len(seq):
        cnt=1
        while i<len(seq)-1 and seq[i]==seq[i+1]:
            cnt+=1
            i+=1
        next_seq+=str(cnt)+seq[i]
        i+=1
    return next_seq

for i in xrange(1, 7):
    print countAndSay(i)