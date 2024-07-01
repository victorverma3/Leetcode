class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = []
        for char in s:
            if char == "*":
                chars.pop()
            else:
                chars.append(char)
        
        return "".join(chars)
        