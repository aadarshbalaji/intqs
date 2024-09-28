class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        prev = intervals[0]
        for start, end in intervals:
            if prev[1] >= start:
                prev[1] = max(prev[1], end)
            else:
                ans.append(prev)
                prev = [start,end]
        ans.append(prev)
        return ans