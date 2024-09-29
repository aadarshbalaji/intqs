class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        currmax = 0
        while l < r:
            currmax = max(currmax, (r-l) * (min(height[l], height[r])))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return currmax
