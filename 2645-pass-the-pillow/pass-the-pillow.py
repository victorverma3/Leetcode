class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        factor = 2 * (n-1)
        time = time % factor
        diff = min(time, factor - time)
        return diff + 1
        