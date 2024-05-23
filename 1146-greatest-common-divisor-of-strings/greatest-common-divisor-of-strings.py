class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def divides(s, x):
            if s == x:
                return True
            elif s[:len(x)] != x:
                return False
            else:
                return divides(s[len(x):], x)

        largest = ""
        i = 1
        while i < max(len(str1), len(str2)) + 1:
            if len(str1) % i == 0 and len(str2) % i == 0:
                x = str1[:i]
                if divides(str1, x) and divides(str2, x):
                    largest = x
            i += 1
        return largest
            
        