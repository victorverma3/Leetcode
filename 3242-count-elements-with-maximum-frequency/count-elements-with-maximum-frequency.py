class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        max_freq = max(counts.values())
        total = 0
        for freq in counts.values():
            if freq == max_freq:
                total += freq
        return total
        