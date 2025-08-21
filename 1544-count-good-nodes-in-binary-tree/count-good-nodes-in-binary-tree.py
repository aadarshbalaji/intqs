# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rv = []
        def search(node, currmax):
            if not node:
                return
            tempcurrmax = currmax
            if node.val >= currmax:
                rv.append(1)
                tempcurrmax = node.val
            search(node.left, tempcurrmax)
            search(node.right, tempcurrmax)
        search(root, -float('inf'))
        return len(rv)