class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = []
        c = Counter(nums)
        for value, freq in c.items():
            heappush(h, [-freq, value])
        rv = []
        for i in range(k):
            if h:
                rv.append(heappop(h)[1])
        return rv
        