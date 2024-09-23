class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def backtrack(node, path):
            path.append(node)
            if node == len(graph) - 1:
                ans.append(list(path))
            for n in graph[node]:
                backtrack(n, path)
            path.pop()
        backtrack(0,[])
        return ans