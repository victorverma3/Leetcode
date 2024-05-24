class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = defaultdict(int)
        count = 0
        for i in range(len(grid)):
            rows[tuple(grid[i])] += 1
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            if tuple(col) in rows:
                count += rows[tuple(col)]
        return count


        return count
        