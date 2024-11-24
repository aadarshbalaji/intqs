# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rv = []
        def helper(node, height):
            if not node:
                return
            if len(rv) == height:
                rv.append(node.val)
            helper(node.right, height+1)
            helper(node.left, height+1)
        helper(root, 0)
        return rv