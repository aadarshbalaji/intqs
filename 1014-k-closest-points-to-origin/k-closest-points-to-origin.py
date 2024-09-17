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
        d.sort()
        return [hs[y].pop(0) for y in d[0:k]]

