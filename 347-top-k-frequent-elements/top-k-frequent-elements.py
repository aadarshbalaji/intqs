class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = [[] for i in range(len(nums)+1)]
        counter = Counter(nums)
        for val, freq in counter.items():
            arr[freq].append(val)
        
        rv = []
        for values in arr[::-1]:
            if len(rv) < k:
                rv.extend(values)
        return rv