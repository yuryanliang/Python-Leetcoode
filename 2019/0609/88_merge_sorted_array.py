def merge(A,m, B, n):
    last=m+n-1
    i=m-1
    j=n-1

    while i>=0 and j>=0:
        if A[i]>B[j]:
            A[last]=A[i]
            last=last-1
            i=i-1
        else:
            A[last]=B[j]
            last=last-1
            j-=1
    while j>=0:
        A[last]=B[j]
        last=last-1
        j=j-1
