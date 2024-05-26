class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        curr_string = []
        curr_letters = set()
        for i in s:
            if i in curr_letters:
                count += 1
                curr_string = [i]
                curr_letters = set([i])
            else:
                curr_string.append(i)
                curr_letters.add(i)
        if curr_string:
            count += 1
        return count
        