class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        ans = 0
        count = 0
        for i, freq in enumerate(sorted(c.values(), reverse=True)):
            if i % 9 == 0:
                count += 1
            ans += freq * count
        return ans