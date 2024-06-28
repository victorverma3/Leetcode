class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqs = defaultdict(int)
        for char in s:
            freqs[char] += 1
        freqs = freqs.items()

        def mergesort(array):
            if len(array) < 2:
                return array[:]
            else:
                mid = len(array) // 2
                left = mergesort(array[:mid])
                right = mergesort(array[mid:])
                return merge(left, right)
        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                print(left, right)
                if left[i][1] > right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result
        
        sorted_freqs = mergesort(freqs)
        string = ""
        for char, count in sorted_freqs:
            string = string + (count * char)
        return string
        