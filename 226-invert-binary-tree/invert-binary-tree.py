# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, tree: Optional[TreeNode]) -> Optional[TreeNode]:
        if tree == None:
            return
        #print(tree.val)
        currleft = tree.left
        tree.left = tree.right
        tree.right = currleft


        self.invertTree(tree.left)
        self.invertTree(tree.right)
        return tree
