# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        currmax = [0]
        def getdepth(node, currdepth):
            if not node:
                currmax[0] = max(currmax[0], currdepth)
                return
            getdepth(node.left, currdepth + 1)
            getdepth(node.right, currdepth + 1)
        
        getdepth(root, 0)
        return currmax[0]


        