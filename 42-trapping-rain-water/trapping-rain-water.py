class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * n
        suff = [0] * n
        outcome = 0
        for i in range(1, n):
            pre[i] = max(pre[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i+1], height[i+1])
        
        for i, h in enumerate(height):
            curr = min(pre[i], suff[i]) - h
            if curr >= 0:
                outcome += curr
        return outcome