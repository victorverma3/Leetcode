class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        count = defaultdict(int)
        for num in nums1:
            count[num] += 1
        for num in nums2:
            if count[num] > 0:
                intersection.append(num)
                count[num] -= 1
        return intersection
        