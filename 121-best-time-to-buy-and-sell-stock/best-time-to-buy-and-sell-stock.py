class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices[1:]:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit

