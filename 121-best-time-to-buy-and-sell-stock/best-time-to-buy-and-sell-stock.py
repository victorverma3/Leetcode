class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxRight = [0] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], prices[i+1])
        
        largest = 0
        lowest = float("inf")
        for i in range(len(prices)):
            if prices[i] >= lowest:
                continue
            else:
                lowest = prices[i]
                largest = max(largest, maxRight[i] - prices[i])
        
        return largest
        