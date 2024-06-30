class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        maxLeft = defaultdict(int)
        maxRight = defaultdict(int)
        maxLeft[0] = 0
        maxRight[len(height)-1] = 0
        for i in range(1, len(height)-1):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
        for i in range(len(height)):
            water += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        return water




        