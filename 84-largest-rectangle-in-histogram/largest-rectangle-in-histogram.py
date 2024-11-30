class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxbig = 0
        for i, num in enumerate(heights):
            start = i
            while stack and stack[-1][1] > num:
                pastindex, pastheight = stack.pop()
                maxbig = max(maxbig, (i - pastindex) * pastheight)
                start = pastindex
            stack.append([start, num])
        
        for i, num in stack:
            maxbig = max(maxbig, num * (len(heights) - i))
        return maxbig




            