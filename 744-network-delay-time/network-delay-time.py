class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = defaultdict(lambda :float('inf')) #start everything  at infinity and then update

        dist[k] = 0
        graph = defaultdict(dict)
        for source, dest, weight in times:
            graph[source][dest] = weight
        
        heap = [] #source, dest
        #dikstras is shortest path alg from source to everything
        #start with source, check the closes edges from current graph, update edge weight and set
        heapq.heappush(heap, (dist[k], k))

        while heap:
            distance, vertex = heappop(heap)
            for connection in graph[vertex].keys():
                ctc = distance + graph[vertex][connection]
                if ctc < dist[connection]:
                    dist[connection] = ctc
                    heappush(heap, (ctc , connection))
        if len(dist.values()) != n:
            return -1
        rv = -float('inf')
        for val in dist.values():
            if val == float('inf'):
                return -1
            rv = max(rv, val)
        return rv
            

            




