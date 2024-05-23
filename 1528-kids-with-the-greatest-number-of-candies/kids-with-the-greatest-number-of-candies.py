class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)
        result = []
        for num in candies:
            if num + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)
        return result