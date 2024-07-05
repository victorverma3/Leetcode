# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        points = []
        position = 0
        prev = head
        trav = head.next
        while trav.next:
            position += 1
            if trav.val < prev.val and trav.val < trav.next.val:
                points.append(position)
            elif trav.val > prev.val and trav.val > trav.next.val:
                points.append(position)
            prev = trav
            trav = trav.next

        if len(points) < 2:
            return [-1, -1]
        
        minDistance = float("inf")
        for i in range(1, len(points)):
            minDistance = min(minDistance, points[i] - points[i-1])
        maxDistance = points[-1] - points[0]

        return [minDistance, maxDistance]


        