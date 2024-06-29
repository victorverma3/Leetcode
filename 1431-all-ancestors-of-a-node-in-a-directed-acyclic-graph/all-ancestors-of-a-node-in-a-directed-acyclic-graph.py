class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        ancestors = defaultdict(list)
        def bfs(source, graph):
            visited = set([source])
            queue = [source]
            while len(queue) > 0:
                node = queue.pop(0)
                if node != source:
                    ancestors[node].append(source)
                for child in graph[node]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)

        for source in range(n):
            bfs(source, graph)

        answer = [[]] * n
        for node in graph.keys():
            answer[node] = ancestors[node]
        return answer