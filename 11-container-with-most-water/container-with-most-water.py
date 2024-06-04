class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        l = 0
        r = len(height) - 1
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            max_water = max(water, max_water)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_water