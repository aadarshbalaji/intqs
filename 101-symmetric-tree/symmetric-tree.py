# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = deque()
        q.append(root)
        q.append(root)
        while q:
            a = q.popleft()
            b = q.popleft()
            if not a and not b:
                continue
            if not a and b or a and not b:
                return False
            if a and b and a.val != b.val:
                return False
            q.append(a.left)
            q.append(b.right)
            q.append(a.right)
            q.append(b.left)
        return True
            