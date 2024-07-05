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
        for index, price in enumerate(prices):
            if price >= lowest:
                continue
            else:
                lowest = price
                largest = max(largest, maxRight[index] - price)
        
        return largest
        