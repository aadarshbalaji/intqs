class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def calc(x, y):
            return (x**2 + y**2) ** 0.5
        
        for xx, yy in points:
            heappush(heap, [-calc(xx,yy), [xx,yy]])
            if len(heap) > k:
                heappop(heap)
        
        rv = []
        while heap and len(rv) < k:
            rv.append(heappop(heap)[1])
        return rv