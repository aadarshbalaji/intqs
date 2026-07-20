class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x**2 + y**2
        
        heap = []
        for xc, yc in points:
            heappush(heap, (dist(xc, yc), [xc,yc]))
        
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        return res