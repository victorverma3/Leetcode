class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        else:
            generated = self.generateParenthesis(n-1)
            result = []
            seen = set()
            for value in generated:
                for i in range(len(value)):
                    if "(" + value[:i] + ")" + value[i:] not in seen:
                        seen.add("(" + value[:i] + ")" + value[i:])
                        result.append("(" + value[:i] + ")" + value[i:])
            return result
        