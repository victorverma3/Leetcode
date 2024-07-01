"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        def bfs(root):
            queue = [(root, 0)]
            while len(queue) > 0:
                node, level = queue.pop(0)
                if len(queue) == 0:
                    node.next = None
                else:
                    if level == queue[0][1]:
                        node.next = queue[0][0]
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        bfs(root)
        
        return root
        