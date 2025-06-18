class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rv = []
        h = []
        freq = Counter(nums)
        for num, count in freq.items():
            heappush(h, [-count, num])
        
        for i in range(k):
            if h:
                rv.append(heappop(h)[1])
        return rv



