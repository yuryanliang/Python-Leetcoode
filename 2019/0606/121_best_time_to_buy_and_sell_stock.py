def maxProfit(prices):
    if len(prices)<=1:
        return 0
    min_price=prices[0]
    max_profit=0

    for i in prices:
        min_price=min(min_price, i)
        max_profit=max(i-min_price,max_profit)
    return max_profit