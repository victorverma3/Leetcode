class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        openP = []
        pairs = []
        for index, char in enumerate(s):
            if char == "(":
                openP.append(index)
            elif char == ")":
                pairs = [(openP.pop(), index, len(pairs))] + pairs
        
        # print(pairs)

        while len(pairs) > 0:
            l, r, f = pairs.pop()
            # print(l, r, f)
            temp = list(s)
            temp[l+1:r] = temp[r-1:l:-1]
            s = "".join(temp)
            # print(s)
        
        answer = ""
        for char in s:
            if char == "(" or char == ")":
                continue
            answer = answer + char
        
        return answer