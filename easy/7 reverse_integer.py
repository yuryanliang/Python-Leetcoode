
# math reverse
class Solution(object):

    def reverse(self, x):
        n = x if x > 0 else -x # need to change to n, otherwise  the lower x sign check, x will be 0
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n //10
        if res > 0x7fffffff:
            return 0
        else:
            return res if x > 0 else -res
def main():
    x = [-123]
    for n in x:
        print(Solution().reverse(n))
if __name__ == '__main__':
    # main_1()
    main()
