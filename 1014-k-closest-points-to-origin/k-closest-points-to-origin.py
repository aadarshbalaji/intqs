class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(arr):
            x = arr[0]
            y = arr[1]
            return ((x)**2 + (y)**2)**0.5
        hs = defaultdict(list)
        d = []
        for arr in points:
            var = dist(arr)
            hs[var].append(arr)
            heappush(d, var)
        return [hs[heapq.heappop(d)].pop(0) for y in range(k)]

