原题
给定每天的股票价格，如果允许进行多次交易，即可以多次买入和卖出，但手中最多只能持有一支股票，在再次买入的时候必须将之前的股票卖出，求能获取的最大利润。
注意点：

无
例子:

输入: prices = [2, 4, 6, 1, 3, 8, 3]
输出: 11([2,6]、[1,8]是两次进行买入卖出的时机)
解题思路
可以进行多次交易的话，为了获取最多的利润，应该在每一段价格上升的区间的开头买入，末尾卖出。从前往后遍历数组，如果价格下跌，则在前一天卖出，在下跌的那天再次买入。不要忘记最后的上升段之后没有下跌的情况，要额外加上。
AC源码
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = high = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                high = prices[i]
            else:
                profit += high - low
                low = high = prices[i]
        profit += high - low
        return profit


if __name__ == "__main__":
    assert Solution().maxProfit([2, 4, 6, 1, 3, 8, 3]) == 11
# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element is 
# the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
#解题思路：由于可以进行无限次的交易，那么只要是递增序列，就可以进行利润的累加
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit
