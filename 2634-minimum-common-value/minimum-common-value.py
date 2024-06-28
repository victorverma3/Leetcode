class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1_set = set(nums1)
        for num in nums2:
            if num in nums1_set:
                return num
        return -1
        