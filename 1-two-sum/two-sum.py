class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previous = {}
        for index, n in enumerate(nums):
            diff = target - n
            if diff in previous:
                return [previous[diff], index]
            else:
                previous[n] = index
                