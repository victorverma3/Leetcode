class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowels = 0
        curr_count = 0
        vowels = set(["a", "e", "i", "o", "u"])

        for char in s[:k]:
            if char in vowels:
                max_vowels += 1
        curr_count = max_vowels

        i = 1
        j = k
        while j < len(s):
            if s[i-1] in vowels:
                curr_count -= 1
            if s[j] in vowels:
                curr_count += 1
            i += 1
            j += 1
            max_vowels = max(max_vowels, curr_count)
    
        return max_vowels
        