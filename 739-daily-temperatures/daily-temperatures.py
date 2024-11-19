class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        rv = [0] * len(temperatures)
        while i < len(temperatures):
            while stack and stack[-1][0] < temperatures[i]:
                prevtemp, previndex = stack.pop()
                rv[previndex] = i - previndex
            stack.append([temperatures[i], i])
            i += 1
        return rv