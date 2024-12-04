class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        prefix = [0] * (len(height) + 1)
        suff = [0] * (len(height) + 1)
        for i, pre in enumerate(height[1:]):
            prefix[i+1] = max(prefix[i], height[i])
        for i in range(len(height)-2,-1,-1):
            suff[i] = max(suff[i+1], height[i+1])
        total = 0
        for i in range(len(height)):
            total += max(0, min(suff[i], prefix[i]) - height[i])
        return total
            