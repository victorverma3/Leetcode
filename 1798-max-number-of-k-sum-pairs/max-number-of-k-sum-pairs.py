class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        count = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            temp = nums[i] + nums[j]
            if temp == k:
                count += 1
                i += 1
                j -= 1
            elif temp < k:
                i += 1
            else:
                j -= 1
        return count

        