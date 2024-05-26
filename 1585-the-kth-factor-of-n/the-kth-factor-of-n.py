class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = {}
        i = 1
        total_count = 0
        count = 0
        while i <= n ** 0.5:
            if n % i == 0:
                count += 1
                factors[count] = (i, n / i)
                if i ** 2 == n:
                    total_count += 1
                else:
                    total_count += 2
            i += 1
        if k > total_count:
            return -1
        elif k > len(factors):
            if total_count % 2 == 0:
                return factors[len(factors) - (k - len(factors)) + 1][1]
            else:
                return factors[len(factors) - (k - len(factors))][1]
        else:
            return factors[k][0]
        