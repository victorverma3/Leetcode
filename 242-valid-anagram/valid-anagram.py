class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1
        return d1 == d2