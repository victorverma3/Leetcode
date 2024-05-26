# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        elif not head.next.next:
            head.next = None
            return head
        prev = head
        curr = head.next
        while curr.next and curr.next.next:
            prev = prev.next
            curr = curr.next.next
        prev.next = prev.next.next
        return head
        