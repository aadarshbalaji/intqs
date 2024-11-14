class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        heap = []
        for num, freq in freq.items():
            heappush(heap, [freq, num])
            if len(heap) > k:
                heappop(heap)
        rv = []
        for i in range(k):
            rv.append(heappop(heap)[1])
        return rv
