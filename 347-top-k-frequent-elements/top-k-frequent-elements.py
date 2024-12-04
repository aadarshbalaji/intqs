class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
       
        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            buckets[count].append(num)
        
        arr = []
        for bucket in buckets[::-1]:
            if len(arr) < k:
                arr.extend(bucket)
        return arr

            

        
        