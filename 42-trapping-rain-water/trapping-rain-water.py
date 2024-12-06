class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        pre = [0] * (len(height) + 1)
        suff = [0] * (len(height) + 1)
        for i in range(1, len(height)):
            pre[i] = max(pre[i -1], height[i-1])
        for i in range(len(height)-2,-1,-1):
            suff[i] = max(suff[i+1],height[i+1])
        
        for j, wall in enumerate(height):
            curr = min(suff[j], pre[j]) - wall
            total += max(0, curr)
        
        return total