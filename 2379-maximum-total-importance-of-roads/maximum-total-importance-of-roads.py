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
        
        # road_counts = count.items()
        #
        # def mergesort(array):
        #     if len(array) < 2:
        #         return array[:]
        #     else:
        #         mid = len(array) // 2
        #         left = mergesort(array[:mid])
        #         right = mergesort(array[mid:])
        #         return merge(left, right)

        # def merge(left, right):
        #     result = []
        #     i = 0
        #     j = 0
        #     while i < len(left) and j < len(right):
        #         if left[i][1] >= right[j][1]:
        #             result.append(left[i])
        #             i += 1
        #         else:
        #             result.append(right[j])
        #             j += 1

        #     while i < len(left):
        #         result.append(left[i])
        #         i += 1
        #     while j < len(right):
        #         result.append(right[j])
        #         j += 1

        #     return result

        # sorted_road_counts = mergesort(road_counts)
        
        # importance = 0
        # for index, city in enumerate(sorted_road_counts):
        #     importance += ((n - index) * city[1])

        # return importance