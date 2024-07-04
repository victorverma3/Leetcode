# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start = head.next
        curr = head.next
        trav = head.next
        count = 0

        while trav.next.next:
            if trav.val != 0:
                count += trav.val
                trav = trav.next
            else:
                curr.val = count
                count = 0
                trav = trav.next
                curr.next = trav
                curr = trav

        count += trav.val
        curr.val = count
        curr.next = None

        return start
        
        