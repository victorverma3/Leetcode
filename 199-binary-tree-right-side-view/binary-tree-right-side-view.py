# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []
        if root is None:
            return values

        def bfs(root):
            queue = [(root, 0)]
            while len(queue) > 0:
                node = queue.pop(0)
                if queue == []:
                    values.append(node[0].val)
                elif queue[0][1] > node[1]:
                    values.append(node[0].val)
                if node[0].left is not None:
                    queue.append((node[0].left, node[1] + 1))
                if node[0].right is not None:
                    queue.append((node[0].right, node[1] + 1))
                
        bfs(root)

        return values
                    