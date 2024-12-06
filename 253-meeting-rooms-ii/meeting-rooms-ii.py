class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        heap = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if heap and start >= heap[0]:
                heapreplace(heap, end)
            else:
                heappush(heap, end)
            i += 1
        return len(heap)
