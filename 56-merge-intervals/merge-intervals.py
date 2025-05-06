class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        currstart, currend = intervals[0]
        new = []
        for start, end in intervals[1:]:
            if start <= currend:
                currend = max(currend, end)
                continue
            if start > currend:
                new.append([currstart, currend])
                currstart, currend = start, end
        new.append([currstart, currend])
        return new
                