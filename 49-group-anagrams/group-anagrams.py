from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hs = defaultdict(list) #counter to list of words
        for word in strs:
            sorted_word = str(sorted(word))
            hs[sorted_word].append(word)
        
        return hs.values()
            
        