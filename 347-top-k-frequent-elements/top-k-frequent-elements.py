class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rv = []
        s = set()
        h = []
        c = Counter(nums)
        for num, occurences in c.items():
            heappush(h, [-occurences, num])
        for i in range(k):
            if h:
                rv.append(heappop(h)[1])
        return rv