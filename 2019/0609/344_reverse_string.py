def reverseString(s):
    string=list(s)
    i=0
    j=len(string)-1

    while i<j:
        string[i],string[j]=string[j],string[i]
        i+=1
        j-=1
    return "".join(string)