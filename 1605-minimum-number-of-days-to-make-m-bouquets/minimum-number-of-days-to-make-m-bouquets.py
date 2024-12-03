class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def canmake(days):
            consecutive = 0
            total = 0
            for num in bloomDay:
                if days >= num:
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive == k:
                    total += 1
                    consecutive = 0
                if total == m:
                    return True
            return False
        print(canmake(5))
        l = 0
        r = max(bloomDay)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            print(l, r)
            if canmake(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
