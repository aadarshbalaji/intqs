class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        start, end = newInterval
        while i < len(intervals) and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1
        if i < len(intervals):
            print(intervals[i])
        curr = newInterval
        while i < len(intervals) and end >= intervals[i][0]:
            curr[0] = min(intervals[i][0], curr[0])
            curr[1] = max(intervals[i][1], end)
            i += 1

        ans.append(curr)

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        
        return ans