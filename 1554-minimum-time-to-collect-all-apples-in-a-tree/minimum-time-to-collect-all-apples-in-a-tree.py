class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)
        
        def traverse(node, parent):
            result = 0
            for connection in graph[node]:
                if connection != parent:
                    result += traverse(connection, node)
            
            if result or hasApple[node]:
                result += 2
            return result
        return max(traverse(0,-1)-2,0)