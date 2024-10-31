class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        optimal = [[None for col in range(len(grid[0]))] for j in range(len(grid))]

        def search(row, col):

            if optimal[row][col]:
                return 1 + optimal[row][col]

            right, down, up = 0, 0, 0
            if col < len(grid[0]) - 1:
                if grid[row][col+1] > grid[row][col]:
                        right = search(row, col+1)
                if row > 0:
                    if grid[row-1][col+1] > grid[row][col]:
                        down = search(row-1, col+1)
                if row + 1 < len(grid):
                    if grid[row+1][col+1] > grid[row][col]:
                        up = search(row+1, col+1)

            optimal[row][col] = max(right, down, up)
            
            return 1 + optimal[row][col] 

        maxMoves = 0
        for i in range(len(grid)):
            maxMoves = max(maxMoves, search(i, 0))
        
        return maxMoves - 1
        