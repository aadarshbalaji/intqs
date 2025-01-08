class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()
        visited.add(0)
        q = deque()
        q.append(0)
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)
                # Remove the back edge to avoid revisiting the parent node
                graph[neighbor].remove(curr)
        return len(visited) == n and len(edges) == n - 1