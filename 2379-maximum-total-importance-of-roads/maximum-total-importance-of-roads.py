class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        count = defaultdict(int)
        for road in roads:
            count[road[0]] += 1
            count[road[1]] += 1

        counts = count.values()
        counts = sorted(counts)[::-1]
        importance = 0
        for index, c in enumerate(counts):
            importance += ((n - index) * c)
        
        return importance
        