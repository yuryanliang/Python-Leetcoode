def isAnagram(s,t):
    discS={}
    discT={}

    for n in s:
        if n not in discS:
            discS[n]=1
        else:
            discS[n]+=1
    for n in t:
        if n not in discT:
            discT[n]=1
        else:
            discS[n]+=1
    return discS==discT