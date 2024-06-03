class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(maze, node):
            visited = set()
            visited.add(node)
            queue = [node]
            parents = {node: None}
            
            while queue != []:
                node = queue.pop(0)
                r = node[0]
                c = node[1]
                if maze[r][c] == "+":
                    continue
                if maze[r][c] == "." and node != tuple(entrance) and (r in [0, m-1] or c in [0, n-1]):
                    length = 0
                    while parents[node] is not None:
                        length += 1
                        node = parents[node]
                    return length
                for d in directions:
                    new = (r+d[0], c+d[1])
                    if 0 <= new[0] < m and 0 <= new[1] < n and new not in visited:
                        visited.add(new)
                        queue.append(new)
                        parents[new] = node
            return -1

        return bfs(maze, tuple(entrance))
        