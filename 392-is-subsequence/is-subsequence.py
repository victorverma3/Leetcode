class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        if s == "":
            return True
        if len(s) > len(t):
            return False
        for i in range(len(t)):
            if t[i] == s[count]:
                count += 1
            if count == len(s):
                return True
        
        return False
        