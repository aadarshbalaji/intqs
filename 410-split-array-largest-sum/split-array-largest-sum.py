class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canmake(cumd):
            count = 1
            currcount = 0
            for num in nums:
                if currcount + num > cumd:
                    count += 1
                    currcount = num
                else:
                    currcount += num
            return count <= k
        l = max(nums)
        r = sum(nums)
        rv = r
        while l < r:
            mid = (l + r) //2
            if canmake(mid):
                r = mid
            else:
                l = mid+1
            rv = min(rv, r)
        return rv



