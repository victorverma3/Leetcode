class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1:
            return float(nums[0])

        i = 0
        j = k
        curr_average = float(sum(nums[i:j])) / k
        max_average = curr_average

        while j < len(nums):
            curr_average = curr_average - float(nums[i]) / k + float(nums[j]) / k
            max_average = max(max_average, curr_average)
            i += 1
            j += 1
            
        return max_average
        
        return max_average
        