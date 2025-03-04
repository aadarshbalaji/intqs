# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rv = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            rv.append(node.val)
            traverse(node.right)
        traverse(root)
        return rv