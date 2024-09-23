# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, small, large):
            if not node:
                return True
            if not (node.val > small and node.val < large):
                return False
            
            return valid(node.left, small, node.val) and valid(node.right, node.val, large)
        
        return valid(root, -float('inf'), float('inf'))