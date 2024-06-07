class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        cities = set(i for i in range(len(isConnected)))
        visited = set()

        def dfs(source, connections, visited):
            links = [j for j in range(len(isConnected)) if j not in visited]
            for j in links:
                if connections[source][j] == 1:
                    visited.add(j)
                    dfs(j, connections, visited)

        provinces = 0
        for c in cities:
            if c not in visited:
                dfs(c, isConnected, visited)
                provinces += 1

        return provinces
        