class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rv = []
        buckets = [[] for i in range(len(nums) +  1)]
        freq = Counter(nums)
        for num, count in freq.items():
            buckets[count].append(num)
        
        for bucket in buckets[::-1]:
            if k - len(rv) >= len(bucket):
                rv.extend(bucket)
        return rv


        


