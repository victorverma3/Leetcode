class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.minimum) > 0:
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.minimum.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minimum.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()