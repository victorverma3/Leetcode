class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_number = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:                       
                if k == 0:                        
                    while nums[j] != 0: 
                        j += 1
                    j += 1
                else: 
                    k -= 1                       
            max_number = max(max_number, i - j + 1)             
        return max_number
        