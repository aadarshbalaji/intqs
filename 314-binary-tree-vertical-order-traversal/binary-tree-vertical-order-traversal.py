# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        columns = defaultdict(list)
        q = deque()
        q.append([root, 0])
        while q:
            node, col = q.popleft()

            if node:
                columns[col].append(node.val)
                q.append([node.left, col-1])
                q.append([node.right, col + 1])
        
        return [columns[x] for x in sorted(columns.keys())]