class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for num in nums1:
            heappush(heap, [num + nums2[0], 0])
        
        rv = []
        while k and heap:
            total_sum, index = heappop(heap)
            rv.append([total_sum-nums2[index], nums2[index]])

            if index + 1 < len(nums2):
                heappush(heap, [(total_sum - nums2[index] + nums2[index+1]), index +1])
            k -= 1
        return rv