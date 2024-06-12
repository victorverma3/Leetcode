class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()
        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                temp = val + nums[left] + nums[right]
                if temp == 0:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
        return triplets