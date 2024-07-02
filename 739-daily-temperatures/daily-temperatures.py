class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(index)
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = index - prev
            stack.append(index)
            
        return answer
        