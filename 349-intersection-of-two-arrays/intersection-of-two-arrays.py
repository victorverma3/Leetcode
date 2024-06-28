class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        answer = []
        for num in nums2_set:
            if num in nums1:
                answer.append(num)
        return answer
        