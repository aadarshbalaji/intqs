# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isvalid(node, currmin, currmax):
            if not node:
                return True
            if not(currmin < node.val < currmax):
                return False
            return isvalid(node.left, currmin, node.val) and isvalid(node.right, node.val, currmax)
        return isvalid(root, -float('inf'), float('inf'))