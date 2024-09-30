# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def traverse(node):
            #left, center, right
            if not node:
                return
            if node.left:
                traverse(node.left)
            if node:
                arr.append(node.val)
                if len(arr) == k:
                    return arr[-1]
            if node.right:
                traverse(node.right)
        traverse(root)
        return arr[k-1]