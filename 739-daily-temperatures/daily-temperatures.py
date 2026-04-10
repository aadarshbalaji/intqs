class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        rv = [0 for i in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, oldtemp = stack.pop()
                rv[index] = i - index
            stack.append([i, temp])
        return rv
        