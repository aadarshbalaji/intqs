class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        i = 1
        while i < len(intervals):
            if curr[1] > intervals[i][0]:
                return False
            curr = intervals[i]
            i += 1
        
        return True