class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_chars = set(["(", "[", "{"])
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in open_chars:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop(-1)
        return stack == []