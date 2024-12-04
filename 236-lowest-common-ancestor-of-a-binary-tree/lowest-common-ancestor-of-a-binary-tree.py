# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        lowest_left = self.lowestCommonAncestor(root.left, p, q)
        lowest_right = self.lowestCommonAncestor(root.right, p, q)
        if lowest_left and lowest_right:
            return root
        return lowest_left or lowest_right