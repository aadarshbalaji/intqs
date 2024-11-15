# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        rv = []
        def weird(node, height):
            if not node:
                return
            if height >= len(rv):
                rv.append(node.val)
            onright = weird(node.right, height + 1)
            onleft = weird(node.left, height + 1)

        weird(root, 0)
        return rv
