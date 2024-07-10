class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for operation in logs:
            if operation == "./":
                continue
            elif operation == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(operation)
        return len(stack)

        