class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda n:n[0])
        i = 0
        new = []
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0],max(intervals[i][1], intervals[i+1][1])]
                intervals.remove(intervals[i+1])
            else:
                i += 1
        return intervals