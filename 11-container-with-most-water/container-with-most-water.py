class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        currmax = -float('inf')
        while l < r:
            currmax = max(currmax, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -=1
                l += 1
        return currmax
