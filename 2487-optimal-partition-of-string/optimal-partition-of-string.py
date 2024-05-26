class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        strings = []
        curr_string = []
        curr_letters = set()
        for i in s:
            if i in curr_letters:
                strings.append("".join(curr_string))
                curr_string = [i]
                curr_letters = set([i])
            else:
                curr_string.append(i)
                curr_letters.add(i)
        if curr_string:
            strings.append("".join(curr_string))
        return len(strings)
        