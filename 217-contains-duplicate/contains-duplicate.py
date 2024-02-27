class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        store = set()
        for n in nums:
            if n in store:
                return True
            else:
                store.add(n)
        return False