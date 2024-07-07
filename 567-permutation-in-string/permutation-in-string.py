class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        counts = defaultdict(int)
        for char in s1:
            counts[char] += 1
        
        curr = defaultdict(int)
        for i in range(len(s1) - 1):
            curr[s2[i]] += 1
        
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            curr[s2[right]] += 1
            if curr == counts:
                return True
            if curr[s2[left]] == 1:
                curr.pop(s2[left])
            else:
                curr[s2[left]] -= 1    
            left += 1
            right += 1
        
        return False