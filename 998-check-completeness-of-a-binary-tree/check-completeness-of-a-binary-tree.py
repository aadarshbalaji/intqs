# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = []
        q.append(root)
        n = False
        while q:
            node = q.pop(0)
            if node:
                if n == True:
                    return False
                else:
                    q.append(node.left)
                    q.append(node.right)
            else:
                n = True
        return True

                