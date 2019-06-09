def addDigits(num):
    while num>9:
        c=0
        while num:
            c+=num%10
            num/=10
        num=c
    return num