class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x : x[1])
        count = 0
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if prev > start:
                count += 1
            else:
                prev = end
        return count
