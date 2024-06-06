class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k == len(nums):
            return nums

        frequencies = defaultdict(int)
        for i in nums:
            frequencies[i] += 1
        freq = [(key, val) for key, val in frequencies.items()]

        def mergesort(array):
            if len(array) < 2:
                return array[:]
            mid = len(array) // 2
            left = mergesort(array[:mid])
            right = mergesort(array[mid:])
            return merge(left, mid, right)

        def merge(left, mid, right):
            helper = []
            i = 0
            j = 0

            while i < mid and j < len(right):
                if left[i][1] > right[j][1]:
                    helper.append(left[i])
                    i += 1
                else:
                    helper.append(right[j])
                    j += 1
            
            while i < mid:
                helper.append(left[i])
                i += 1
            while j < len(right):
                helper.append(right[j])
                j += 1
            
            return helper

        sorted_freq = mergesort(freq)
        most_freq = [freq[0] for freq in sorted_freq]
        return most_freq[:k]