def isPowerOfThree(n):
    if n<=0:
        return False
    while n%3==0:
        n/=3
    return n==1
def isPowerOfThree1(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%3==0:
        return isPowerOfThree1(n/3)
    else:
        return False