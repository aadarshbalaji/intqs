class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        seen = {}
        currmax = 0
        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            currmax = max(currmax, r-l+1)
            seen[c] = r
        return currmax

