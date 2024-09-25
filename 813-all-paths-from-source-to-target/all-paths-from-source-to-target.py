class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(index, path):
            path.append(index)
            if index == len(graph)-1:
                ans.append(list(path))
            for n in graph[index]:
                dfs(n, path)
            path.pop()
        dfs(0, [])
        return ans
