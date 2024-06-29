class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        transformation = "" + str(n) + str(2*n) + str(3*n)
        digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        return len(transformation) == 9 and set(transformation) == digits
        