class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for string in strs:
            sorted_tuple = tuple(sorted(string))
            anagrams[sorted_tuple].append(string)
        return anagrams.values()
            