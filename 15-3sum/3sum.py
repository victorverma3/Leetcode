class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triples = []
        seen = set()
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            track = set()
            for j in range(i+1, len(nums)):
                if target - nums[j] in track:
                    if tuple([nums[i], target - nums[j]]) not in seen:
                        seen.add(tuple([nums[i], target - nums[j]]))
                        triples.append([nums[i], target - nums[j], nums[j]])
                track.add(nums[j])
        return triples