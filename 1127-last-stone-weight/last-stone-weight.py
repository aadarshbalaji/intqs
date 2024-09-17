class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-1*s for s in stones]
        heapq.heapify(h)
        print(h)
        while len(h) > 1:
            first = -1 * heapq.heappop(h)
            second = -1 * heapq.heappop(h)
            diff = abs(first-second)
            if diff != 0:
                heapq.heappush(h, -diff)
        
        return -h[0] if len(h)==1 else 0