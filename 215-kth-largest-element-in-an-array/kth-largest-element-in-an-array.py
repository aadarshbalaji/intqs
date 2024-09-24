class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)

        for i in range(len(nums)-k+1):
            x = heapq.heappop(heap)
        return x