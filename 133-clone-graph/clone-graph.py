"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        hs = {} #mapping node.val of original graph to new node
        node_set = set()
        dih = defaultdict(list)
        def explore(node):
            if not node or node.val in node_set:
                return 
            node_set.add(node.val)
            hs[node.val] = Node(node.val)
            for neigh in node.neighbors:
                dih[node.val].append(neigh.val)
                if neigh.val not in node_set:
                    explore(neigh)
        explore(node)
        
        for i in node_set:
            for nint in dih[i]:
                hs[i].neighbors.append(hs[nint])
        
        return hs[node_set.pop()] if node_set else None



        