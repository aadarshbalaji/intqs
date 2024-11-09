class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        new = []
        curr = intervals[0]
        for start, end in intervals[1:]:
            if start <= curr[1]:
                curr[1] = max(curr[1], end)
            else:
                new.append(curr)
                curr = [start,end]
        
        new.append(curr)
        return new
        