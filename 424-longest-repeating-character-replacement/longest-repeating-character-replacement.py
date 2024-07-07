class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0
        left = 0
        right = 0
        count = defaultdict(int)

        while right < len(s):
            count[s[right]] += 1
            max_key = max(count, key=count.get)

            while (right - left + 1) - count[max(count, key=count.get)] > k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest

        