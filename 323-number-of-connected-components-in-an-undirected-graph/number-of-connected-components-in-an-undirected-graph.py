class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for i in range(n):
            #print(i, 'loommoo', visited)
            if i not in visited:
                dfs(i)
                count += 1
        return count
