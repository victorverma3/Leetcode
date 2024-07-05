class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        largest = 0
        left = 0
        right = 1
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                largest = max(largest, prices[right] - prices[left])
            right += 1
        
        return largest
        