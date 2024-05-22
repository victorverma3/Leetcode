class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        minLength = min(len(word1), len(word2))

        for i in range(minLength):
            result.extend([word1[i], word2[i]])
        result.extend([word1[minLength:], word2[minLength:]])

        return ''.join(result)