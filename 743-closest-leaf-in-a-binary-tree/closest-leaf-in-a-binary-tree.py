# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        q = deque()
        k_node = [None]
        leaves = set()
        def create_graph(node, parent):
            if not node:
                return 
            if node.val == k:
                k_node[0] = node
            if not node.left and not node.right:
                leaves.add(node)
            if parent:
                graph[parent].append(node)
                graph[node].append(parent)
            create_graph(node.left, node)
            create_graph(node.right, node)
            
        create_graph(root, None)
        #print(graph)
        if k_node[0] in leaves:
            return k_node[0].val
        q.append(k_node[0])
        count = 1
        seen = set()
        while q:
            node = q.popleft()
            seen.add(node)
            if node in leaves:
                return node.val
            for neighbor in graph[node]:
                if neighbor not in seen:
                    q.append(neighbor)
            count += 1

            