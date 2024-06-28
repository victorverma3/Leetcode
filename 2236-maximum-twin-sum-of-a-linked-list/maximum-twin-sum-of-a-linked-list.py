# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        n = 0
        twin1s = []
        trav = head
        while trav:
            n += 1
            twin1s.append(trav.val)
            trav = trav.next
        twin1s = twin1s[:n/2]
        
        prev = None
        trav = head
        while trav:
            temp = trav.next
            trav.next = prev
            prev = trav
            trav = temp

        twin2s = []
        trav = prev
        while trav:
            twin2s.append(trav.val)
            trav = trav.next
        twin2s = twin2s[:n/2]

        max_twin_sum = 0
        for i in range(n/2):
            max_twin_sum = max(max_twin_sum, twin1s[i] + twin2s[i])
        return max_twin_sum
        