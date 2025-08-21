# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        rv = []
        q = deque()
        q.append(root)
        if not root:
            return []
        while q:
            currlevel = []
            for i in range(len(q)):
                node = q.popleft()
                currlevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            rv.append(currlevel)
        return rv

            
