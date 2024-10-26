class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        currmax = 0
        while l < r:
            currmax = max(currmax, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r-=1
        return currmax
            