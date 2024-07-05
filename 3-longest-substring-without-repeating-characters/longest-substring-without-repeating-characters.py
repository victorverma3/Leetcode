class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, left, right = 0, 0, 0
        chars = set()

        while right < len(s):
            if s[right] in chars:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
            else:
                longest = max(longest, right - left + 1)     
            chars.add(s[right])
            right += 1

        return longest   