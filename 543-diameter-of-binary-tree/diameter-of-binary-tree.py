# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.currmax = -float('inf')
        def max_height(node):
            if not node:
                return 0
            l = max_height(node.left)
            r = max_height(node.right)

            self.currmax = max(self.currmax, l+r)
            return 1 + max(l,r)
        
        max_height(root)
        return self.currmax
        
