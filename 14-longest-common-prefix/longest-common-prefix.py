class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        curr = ''
        word = min(strs, key = lambda x: len(x))
        for c in word:
            curr = curr + c
            length = len(curr)
            for w in strs:
                if w[0:length] == curr:
                    continue
                else:
                    return curr[0:-1]
        return curr