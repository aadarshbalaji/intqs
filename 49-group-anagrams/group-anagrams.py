from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hs = defaultdict(list) #counter to list of words
        for word in strs:
            buckets = [0 for i in range(26)]
            for letter in word:
                buckets[ord('a')-ord(letter)] += 1
            hs[str(buckets)].append(word)
        return [v for v in hs.values()]

            
        