# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(tree):
            if not tree:
                return 0
            leftheight = helper(tree.left)
            rightheight = helper(tree.right)
            if leftheight == -1 or rightheight == -1:
                return -1
            if abs(leftheight - rightheight) > 1:
                return -1
            else:
                return max(leftheight, rightheight) + 1
        return helper(root) != -1
            
        