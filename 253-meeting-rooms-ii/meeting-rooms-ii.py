class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[0])
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            if start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
        return len(heap)