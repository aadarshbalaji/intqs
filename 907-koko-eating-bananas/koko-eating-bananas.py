class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def caneat(num, new):
            for p in piles:
                new -= math.ceil(p/num)
                if new < 0:
                    return False
            return True
        
        while l < r:
            mid = (l + r )//2
            if caneat(mid, h):
                r = mid
            else:
                l = mid + 1
        return r