# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = []
        leaves2 = []
        def dfs(leaves, root):
            if root is None:
                return None
            if root.left is None and root.right is None:
                leaves.append(root.val)
            else:
                dfs(leaves, root.left)
                dfs(leaves, root.right)
        dfs(leaves1, root1)
        dfs(leaves2, root2)
        return leaves1 == leaves2
        