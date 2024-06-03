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
        left = 1
        right = n
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right
        while left <= right:
            mid = (left + right) >> 1
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                left = mid
            else:
                right = mid
        