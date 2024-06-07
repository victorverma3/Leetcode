class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()

        def dfs(source, connections, visited):
            for j in range(len(isConnected)):
                if j not in visited:
                    if connections[source][j] == 1:
                        visited.add(j)
                        dfs(j, connections, visited)

        provinces = 0
        for c in range(len(isConnected)):
            if c not in visited:
                dfs(c, isConnected, visited)
                provinces += 1

        return provinces
        