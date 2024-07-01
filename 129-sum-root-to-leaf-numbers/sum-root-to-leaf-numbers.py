# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        numbers = []
        
        def dfs(root, number):
            if not root:
                return
            if not root.left and not root.right:
                numbers.append(number + str(root.val))
            dfs(root.left, number + str(root.val))
            dfs(root.right, number + str(root.val))
        dfs(root, "")

        numbers = [int(number) for number in numbers]
        return sum(numbers)

        