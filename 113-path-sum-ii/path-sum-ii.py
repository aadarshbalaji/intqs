# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        arr = []
        def helper(node, path):
            if sum(path) == targetSum and not node.right and not node.left:
                arr.append(list(path))
            if not node:
                return
            if node.left:
                path.append(node.left.val)
                helper(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                helper(node.right, path)
                path.pop()
        
        helper(root, [root.val])
        return arr
            

            
                