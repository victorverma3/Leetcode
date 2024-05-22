class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = len(word1)
        l2 = len(word2)
        string = ""
        if l1 < l2:
            for i in range(l1):
                string = string + word1[i] + word2[i]
            string += word2[l1:]
        else:
            for i in range(l2):
                string = string + word1[i] + word2[i]
            string += word1[l2:]
        return string