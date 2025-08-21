# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        leaves = set()
        def create_graph(node, parent):
            if not node:
                return
            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if not node.left and not node.right:
                leaves.add(node.val)
            create_graph(node.left, node)
            create_graph(node.right, node)
        create_graph(root, None)
        q = deque()
        q.append(k)
        seen = set([k])
        while q:
            node = q.popleft()
            if node in leaves:
                return node
            
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    q.append(neighbor)
        return k
