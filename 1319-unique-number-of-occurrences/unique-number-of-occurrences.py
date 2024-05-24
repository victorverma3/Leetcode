class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = defaultdict(int)

        for i in arr:
            count[i] += 1
        
        return len(count.values()) == len(set(count.values()))