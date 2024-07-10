class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for operation in logs:
            if operation == "../":
                if len(stack) > 0:
                    stack.pop()
            elif operation == "./":
                continue
            else:
                stack.append(operation)
        return len(stack)

        