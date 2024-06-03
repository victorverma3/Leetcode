# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                left = mid
            else:
                right = mid
        