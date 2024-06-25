class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                temp = num + 1
                while temp in nums_set:
                    temp += 1
                longest = max(longest, temp - num)

        return longest
