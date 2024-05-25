class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1 = []
        ans2 = []
        for n in nums1:
            if n not in nums2:
                ans1.append(n)
        for n in nums2:
            if n not in nums1:
                ans2.append(n)

        return [ans1, ans2]