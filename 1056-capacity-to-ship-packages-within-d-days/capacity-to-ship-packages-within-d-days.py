class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canship(day):
            count = 1
            curr = day
            for w in weights:
                if w > day:
                    return False
                if curr < w:
                    count += 1
                    curr = day
                curr -= w
            return count <= days
        

        print(canship(5))
        l = 1
        r = sum(weights)
        val = r
        while l <= r:
            mid = (l+r) // 2
            if canship(mid):
               val = mid
               r = mid - 1
            else:
                l = mid + 1
        return val 
        