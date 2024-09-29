# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            if node:
                arr.append(node.val)
                if len(arr) == k:
                    return 
            if node.right:
                inorder(node.right)
        inorder(root)
        return arr[k-1]