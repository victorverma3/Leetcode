class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        answer = []
        for i in range(len(positives)):
            answer.extend([positives[i], negatives[i]])
        return answer
        