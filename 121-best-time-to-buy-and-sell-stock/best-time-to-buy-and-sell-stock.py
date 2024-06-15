class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        left = 0
        right = 1
        while right < len(prices):
            curr = prices[right] - prices[left]
            if prices[left] < prices[right]:
                p = max(p, curr)
            else:
                left = right
            right += 1
        return p