class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        edgeCount = defaultdict(int)
        for edge in edges:
            edgeCount[edge[0]] += 1
            edgeCount[edge[1]] += 1
        
        for edge in edgeCount:
            if edgeCount[edge] == len(edgeCount) - 1:
                return edge