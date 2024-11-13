"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        hs = {}
        q = deque()
        visited = set()
        q.append(node)
        while q:
            n = q.popleft()
            if n in visited:
                continue
            if n not in hs:
                hs[n] = Node(n.val)
            visited.add(n)
            for neigh in n.neighbors:
                if neigh not in hs:
                    hs[neigh] = Node(neigh.val)
                hs[n].neighbors.append(hs[neigh])
                q.append(neigh)
                
        return hs[node]


            
        