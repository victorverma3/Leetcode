class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        i = 0
        j = len(height) - 1
        while i < j:
            temp_height = min(height[i], height[j])
            temp_width = j-i
            max_water = max(max_water, temp_height * temp_width)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
        