class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def area(left, right):
            return min(height[left], height[right]) * (right-left)
        left = 0
        right = len(height) - 1
        m = area(left, right)
        while left < right:
            m = max(m, area(left, right))
            if min(height[left], height[right]) == height[left]:
                left += 1
            else:
                right -= 1       
        return m
        