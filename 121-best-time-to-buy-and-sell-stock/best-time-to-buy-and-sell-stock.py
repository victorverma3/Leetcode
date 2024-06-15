class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        left = 0
        right = 1
        largestProfit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                largestProfit = max(largestProfit, prices[right] - prices[left])
            right += 1
        return largestProfit

