class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = [i for i in range(1, n+1)]
        while len(friends) > 1:
            leave = k % len(friends)
            if leave == 0:
                friends = friends[:-1]
            else:
                friends = friends[leave:] + friends[:leave-1]
        return friends[0]

        