class DSU:
    def __init__(self, n):
        self.father = [-1 for i in range(n + 1)]
    
    def find(self, x):
        while self.father[x] != -1:
            x = self.father[x]
        #self.father[x] = y
        return x
    
    def union(self, x, y):
        x_father = self.find(x)
        y_father = self.find(y)

        self.father[x_father] = y_father
    


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        for source, dest in edges:
            visited.add(source)
            visited.add(dest)
        
        n = len(visited)

        dsu = DSU(n)
        curr_edge = None

        for source, dest in edges:
            father_source = dsu.find(source)
            father_dest = dsu.find(dest)
            if father_source == father_dest:
                curr_edge = [source, dest]
            else:
                dsu.union(source, dest)
            
        return curr_edge
        


        
