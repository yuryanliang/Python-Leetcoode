def isPalindrome(x):
    if x<0:
        return False
    copy=x
    reverse=0
    while copy>0:
        reverse=reverse *10+copy%10
        copy/=10
    return x==reverse