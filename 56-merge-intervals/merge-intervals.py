class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 1
        rv = []
        curr = intervals[0]
        while i < len(intervals):
            if intervals[i][0] > curr[1]:
                rv.append(curr)
                curr = intervals[i]
                i += 1
            else:
                curr = [min(curr[0], intervals[i][0]), max(intervals[i][1], curr[1])]
                i += 1
        
        rv.append(curr)
        return rv