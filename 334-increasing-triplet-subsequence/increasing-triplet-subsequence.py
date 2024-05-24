class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = "inf"
        second_smallest = "inf"
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else:
                return True
        return False
