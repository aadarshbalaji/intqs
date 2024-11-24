# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(lower=-float('inf'), upper=float('inf')):
            nonlocal index
            if index == len(preorder):
                return None
            val = preorder[index]
            if val < lower or val > upper:
                return None
            node = TreeNode(val)
            index += 1
            node.left = helper(lower, val)
            node.right = helper(val, upper)
            return node
        index = 0
        return helper()

        
            
