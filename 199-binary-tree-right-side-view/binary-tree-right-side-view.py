# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return None
        def weird(node, height):
            if not node:
                return
            if len(ans) <= height:
                ans.append(node.val)
            weird(node.right, height + 1)
            weird(node.left, height + 1)
        weird(root, 0)
        return ans
        