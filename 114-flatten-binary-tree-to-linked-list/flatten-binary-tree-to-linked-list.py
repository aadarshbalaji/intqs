# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def helper(node):
            if not node:
                return None
            if not node.right and not node.left:
                return node
            temp = node.right
            if node.left:
                node.right = helper(node.left)
                node.left = None
                currright = node.right
                while currright and currright.right:
                    currright = currright.right
            
                currright.right = helper(temp)
            else:
                node.right = helper(temp)
            return node
        
        helper(root)

