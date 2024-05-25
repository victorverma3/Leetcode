class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_size = 0
        r = 0
        count = 1
        if sum(nums) == 0:
            return 0
        for l in range(len(nums)):
            if nums[l] == 0:
                if count == 0:
                    while nums[r] != 0: 
                        r += 1
                    r += 1
                else: 
                    count -= 1                       
            max_size = max(max_size, l - r)             
        return max_size
        