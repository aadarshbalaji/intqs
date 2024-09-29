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
        def helper(node, height):
            if not node:
                return height
            else:
                return max(helper(node.right, height+1), helper(node.left, height+1))
        left = helper(root.left,0)
        right = helper(root.right,0)
        if abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

        
            

        