class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        heap = []
        for num, frequency in freq.items():
            heapq.heappush(heap, (-frequency, num))
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
