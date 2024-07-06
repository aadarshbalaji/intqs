# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverthelper(tree):
            if tree == None:
                return
            #print(tree.val)
            currleft = tree.left
            tree.left = tree.right
            tree.right = currleft


            inverthelper(tree.left)
            inverthelper(tree.right)
        inverthelper(root)
        return root
