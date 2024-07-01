class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        one = False
        two = False
        three = False
        for num in arr:
            one = two
            two = three
            three = (num % 2 == 1)
            if one and two and three:
                return True
        return False
        