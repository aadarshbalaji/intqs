class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapify(g)
        heapify(s)
        
        count = 0
        while g and s:
            smallest_child = heappop(g)
            smallest_cookie = heappop(s)
            while smallest_child > smallest_cookie and s:
                smallest_cookie = heappop(s)
            if smallest_cookie >= smallest_child:
                count += 1
        return count