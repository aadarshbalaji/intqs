class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxarea = (r-l) * min(height[r], height[l])
        while l <= r:
            maxarea = max(maxarea, (r-l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea