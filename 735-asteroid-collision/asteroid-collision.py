class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if stack:
                if a * stack[-1] >= 0 or (a > 0 and stack[-1] < 0):
                    stack.append(a)
                else:
                    while True:
                        if not stack:
                            stack.append(a)
                            break
                        elif a * stack[-1] >= 0 or (a > 0 and stack[-1] < 0):
                            stack.append(a)
                            break
                        elif abs(a) == abs(stack[-1]):
                            stack.pop()
                            break
                        elif abs(a) > abs(stack[-1]):
                            stack.pop()
                        else:
                            break
            else:
                stack.append(a)
        return stack
        