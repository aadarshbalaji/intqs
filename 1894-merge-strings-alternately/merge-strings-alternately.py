class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minword = min(word1, word2, key = len)
        new = ''
        for i in range(len(minword)):
            new = new + word1[i] + word2[i]
        
        new += max(word1, word2, key=len)[i+1:]
        return new