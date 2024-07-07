class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        count = 0
        full = numBottles
        empty = 0
        while full + empty >= numExchange:
            count += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
        return count + full
        