class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rv = []
        newstart = newInterval[0]
        newend = newInterval[1]
        i = 0
        n = len(intervals)
        while i < n and newstart > intervals[i][0]:
            rv.append(intervals[i])
            i += 1
        
        if not rv or rv[-1][1] < newstart:
            rv.append(newInterval)
        else:
            rv[-1][1] = max(rv[-1][1], newend)
        
        while i < n:
            start, end = intervals[i]
            if rv[-1][1] < start:
                rv.append(intervals[i])
            else:
                rv[-1][1] = max(rv[-1][1], end)
            i += 1
        return rv

