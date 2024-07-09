class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        finish = [0] * len(customers)
        finish[0] = customers[0][0] + customers[0][1]
        for i in range(1, len(customers)):
            finish[i] = max(finish[i-1], customers[i][0]) + customers[i][1]
        
        wait = 0
        for i in range(len(customers)):
            wait += finish[i] - customers[i][0]

        return float(wait) / len(customers)
        