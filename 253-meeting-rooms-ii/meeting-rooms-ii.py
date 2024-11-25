class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and start >= heap[0]:
                heapreplace(heap, end)
            else:
                heappush(heap, end)
        return len(heap)