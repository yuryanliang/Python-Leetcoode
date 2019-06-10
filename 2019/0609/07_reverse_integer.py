def reverse(x):
    answer=0
    sign=1 if x >0 else -1
    x=abs(x)
    while x>0:
        answer=answer*10+x%10
        x/=10
    return sign*answer if answer<=0x7fffffff else 0