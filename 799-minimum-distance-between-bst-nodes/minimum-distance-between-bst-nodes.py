# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        rv = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            rv.append(node.val) 
            dfs(node.right)
        dfs(root)
        currmin = float('inf')
        for i in range(0, len(rv)-1):
            currmin = min(currmin, rv[i+1]-rv[i])
        return currmin