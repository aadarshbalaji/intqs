class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        currmax = 0
        seen= {}
        for r, c in enumerate(s):
            if c in seen:
                if seen[c] >= l:
                    l = seen[c] + 1

            seen[c] = r
            currmax = max(currmax, r-l+1)
        return currmax
