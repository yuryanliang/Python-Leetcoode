def generate(numRows):
    if numRows == 0:
        return []
    res = [[1]]
    for i in range(1, numRows):
        res.append([])
        for j in range(i + 1):
            left = (res[i - 1][j - 1] if j > 0 else 0)
            right = (res[i - 1][j] if j < i else 0)
            res[i].append(left + right)
        return res

def generate1(numRows):
    res=[]
    for i in range(0,numRows):
        res.append([1]*(i+1))
        for j in range(1, i):
            res[i][j]=res[i-1][j-1]+res[i-1][j]


    return res
print generate1(4)