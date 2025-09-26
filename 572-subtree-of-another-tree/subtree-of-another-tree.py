# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node:
                return False
            if check_same(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        
        def check_same(tree1, tree2):
            if tree1 is tree2:
                return True
            if (tree1 and not tree2) or (tree2 and not tree1):
                return False
            if tree1.val != tree2.val:
                return False
            return check_same(tree1.left, tree2.left) and check_same(tree1.right, tree2.right)
        
        return dfs(root)