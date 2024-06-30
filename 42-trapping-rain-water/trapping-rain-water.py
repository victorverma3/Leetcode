class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        for i in range(1, len(height)-1):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
        for i in range(len(height)):
            water += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        return water




        