# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return helper(node.right, node.val, upper) and helper(node.left, lower, node.val)
        return helper(root, -float('inf'), float('inf'))