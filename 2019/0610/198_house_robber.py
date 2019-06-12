def rob(num):
    size=len(num)
    dp=[0]*(size+1)
    if size:
        dp[1]=num[0]
    for i in range(2, size+1):
        dp[i]=max(dp[i-1], dp[i-2]+num[i-1])
    return dp[size]

rob([2,1,1,2])