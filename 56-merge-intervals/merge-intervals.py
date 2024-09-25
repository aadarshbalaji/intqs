class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        ans = []
        for start, end in intervals[1:]:
            if start <= prev[1]:
                prev[1] = max(prev[1], end)
            else:
                ans.append(prev)
                prev = [start, end]
        ans.append(prev)
        return ans