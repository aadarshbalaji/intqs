# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        rv = []
        def dfs(node, currsum):
            currsum = currsum * 10 + node.val
            if not node.right and not node.left:
                rv.append(currsum)
                return
            if node.right:
                dfs(node.right, currsum)
            if node.left:
                dfs(node.left, currsum)
        dfs(root, 0)
        return sum(rv)


