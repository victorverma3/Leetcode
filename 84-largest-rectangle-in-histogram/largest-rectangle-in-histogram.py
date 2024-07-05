class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        largest = 0
        stack = []
        for index, val in enumerate(heights):
            if not stack or val > stack[-1][1]:
                stack.append((index, val))
            else:
                while stack and val <= stack[-1][1]:
                    top = stack.pop()
                    largest = max(largest, (index - top[0]) * top[1])
                stack.append((top[0], val))
                
        for item in stack:
            largest = max(largest, (len(heights) - item[0]) * item[1])

        return largest
        