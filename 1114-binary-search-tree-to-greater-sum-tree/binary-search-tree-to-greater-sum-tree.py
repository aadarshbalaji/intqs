# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #right, node, left
        runningsum = 0
        def search(node):
            if not node:
                return
            nonlocal runningsum
            search(node.right)
            runningsum += node.val
            node.val = runningsum
            search(node.left)
        search(root)
        return root