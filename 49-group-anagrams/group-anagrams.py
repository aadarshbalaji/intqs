class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for word in strs:
            newword = sorted(word)
            newword = str(newword)
            hs[newword].append(word)
        return [x for x in hs.values()]
