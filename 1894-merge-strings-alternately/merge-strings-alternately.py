class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ww = True
        rv = ""
        t = 0
        b = 0
        while t < len(word1) and b < len(word2):
            if ww:
                rv += word1[t]
                t += 1
            else:
                rv += word2[b]
                b += 1
            ww = not ww
        
        rv += word1[t:]
        rv += word2[b:]
        return rv