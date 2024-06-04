class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        if n == 2:
            return 1

        one, two, three = 0, 1, 1

        for i in range(3, n+1):
            one, two, three = two, three, one + two + three
        
        return three