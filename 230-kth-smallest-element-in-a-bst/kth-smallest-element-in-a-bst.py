# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = []
        def lrr(tree):
            if tree.left:
                lrr(tree.left)
            if tree:
                ordered.append(tree.val)
            if tree.right:
                lrr(tree.right)
        lrr(root)
        return ordered[k-1]