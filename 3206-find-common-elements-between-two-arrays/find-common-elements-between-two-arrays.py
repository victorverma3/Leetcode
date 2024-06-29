class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        answer = []
        count = 0
        for num in nums1:
            if num in nums2_set:
                count += 1
        answer.append(count)
        count = 0
        for num in nums2:
            if num in nums1_set:
                count += 1
        answer.append(count)
        return answer
        