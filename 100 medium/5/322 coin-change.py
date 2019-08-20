"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


"""




# backtracking/brute force
class Solution(object):
    import sys
    res = sys.maxsize
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """


        n = len(coins)
        start = n - 1
        cur = 0
        coins.sort()
        self.helper(coins, start, amount, cur, self.res)
        import sys
        return self.res if self.res != sys.maxsize else -1

    def helper(self, coins, start, target, cur, result):
        if target < 0:
            return
        elif target == 0:
            result =1
            return
        for i in reversed(range(0, start + 1)):
            self.helper(coins, i, target - coins[i], cur + 1, result)


if __name__ == '__main__':
    a = Solution()
    print(a.coinChange([1, 2, 5], 11))
    # print(a.coinChange([70, 71], 142))
    # print(a.coinChange([70, 177, 394, 428, 427, 437, 176, 145, 83, 370], 7582))
