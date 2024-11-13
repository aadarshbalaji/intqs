class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        currmax = 0
        for index, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            currmax = max(currmax, index-l+1)
            seen[c] = index
        return currmax
                
