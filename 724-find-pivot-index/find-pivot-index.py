class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        left_sum = 0
        right_sum = sum(nums)

        i = 0
        while i < len(nums):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            i += 1
        
        return -1