class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def canfinish(k):
            hours = 0
            for bananas in piles:
                if bananas <= k:
                    hours += 1
                else:
                    hours += (bananas//k) + (1 if bananas % k != 0 else 0)
            if hours <= h:
                return True
            return False

        if (h < len(piles)):
            return False
        low = 1
        high = max(piles)
        curmin = max(piles)
        while low <= high:
            midk = (low + high) // 2
            if canfinish(midk):
                curmin = min(curmin, midk)
                high = midk - 1
            else:
                low = midk + 1
            

        return curmin


        