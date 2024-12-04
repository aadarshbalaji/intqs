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
            if not node or len(curr) >= k:
                return
            search(node.left)
            curr.append(node.val)
            search(node.right)
        search(root)
        return curr[k-1]
            