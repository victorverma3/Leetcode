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
            
        memo = [0] * (n+1)
        memo[0], memo[1], memo[2] = 0, 1, 1

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
        return memo[n]