class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        m = 0
        se = set()
        for j in range(len(s)):
            while s[j] in se:
                se.remove(s[i])
                i += 1
            se.add(s[j])
            m = max(m, j - i + 1)
        return m

