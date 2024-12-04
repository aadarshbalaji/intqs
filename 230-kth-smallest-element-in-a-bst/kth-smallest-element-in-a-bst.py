# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = []
        def search(node):
            if not node:
                return
            search(node.left)
            curr.append(node.val)
            if len(curr) == k:
                return curr[-1]
            search(node.right)
        search(root)
        return curr[k-1]