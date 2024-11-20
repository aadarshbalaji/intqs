class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #array method O(n) time complexity
        arr = [[] for i in range(len(nums)+ 1)] 
        freq = Counter(nums)
        for num, count in freq.items():
            arr[count].append(num)
        rv = []
        #print(arr)
        for i in range(len(arr) -1, -1,-1):
            if k == 0:
                return rv
            if arr[i]:
                k -= len(arr[i])
                rv.extend(arr[i])
        return rv
                 
