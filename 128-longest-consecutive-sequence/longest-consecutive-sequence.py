class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set:
                sequence = []
                i = n
                while i in nums_set:
                    sequence.append(i + 1)
                    i += 1
                longest = max(longest, len(sequence))
        return longest