class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        def search(index, path):
            path.append(index)
            if index == len(graph) - 1:
                ans.append(list(path))
            for n in graph[index]:
                search(n, path)
            path.remove(index)
        

        search(0,[])
        return ans