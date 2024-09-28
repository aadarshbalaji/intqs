# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = []
        q.append(root)
        flag = False #true if we have seen a null node

        while q:
            curr = q.pop(0)
            if curr == None:
                flag = True
            else:
                if flag == True:
                    return False
                q.append(curr.left)
                q.append(curr.right)

        return True
                
            