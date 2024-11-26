class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)

        def canship(capacity):
            curr = 0
            i = 0 
            d = days
            while i < len(weights):
                if d < 0:
                    return False
                if curr + weights[i] <= capacity:
                    curr += weights[i]
                    i += 1
                elif weights[i] > capacity or curr + weights[i] > capacity:
                    curr = 0
                    d -= 1
            d -= 1
            return d >= 0
        while l < r:
            mid = (l+r)//2
            if canship(mid):
                r = mid
            else:
                l = mid + 1
        return l
