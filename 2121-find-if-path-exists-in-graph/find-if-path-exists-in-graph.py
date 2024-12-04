class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        q = deque()
        q.append(source)
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            visited[curr] = True
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return False