# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        rv = [0]
        def traverse(node, max_of_path):
            if not node:
                return
            if node.val >= max_of_path:
                rv[0] += 1
            if node.left:
                traverse(node.left, max(max_of_path, node.val))
            if node.right:
                traverse(node.right, max(max_of_path, node.val))
        traverse(root, -float('inf'))
        return rv[0]