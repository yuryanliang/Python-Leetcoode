def climbStairs(n):
    pre = cur = 1
    for i in xrange(1, n):
        pre, cur = cur, pre + cur
    return cur
