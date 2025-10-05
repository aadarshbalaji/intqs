# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:


        arr = []
        def recurse(node):
            if not node:
                return 
            if not node.left and not node.right:
                arr[-1].append(node.val)
                node = None
                return None
            
            if node.left:
                node.left = recurse(node.left)
            if node.right:
                node.right = recurse(node.right)
            return node
        
        while root:
            arr.append([])
            root = recurse(root)
        return arr


