class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxL = height[0]
        maxR = height[-1]
        total = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r]
        return total