def myAtoi(str):
    INT_MAX= 2147483647
    INT_MIN= -2147483647
    result =0
    
    if not str:
        return result
    i=0
    while i <len(str) and str[i].isspace():
        i+=1
    
    sign =1
    if str[i]=="+":
        i+=1
    elif str[i]=="-":
        sign =-1
        i+=1
    
    while i <len(str) and '0'<= str[i]<="9":
        if result>(INT_MAX-int(str[i]))/10:
            return INT_MAX if sign>0 else INT_MIN
        
        result= result*10 + int(str[i])
    return sign*result