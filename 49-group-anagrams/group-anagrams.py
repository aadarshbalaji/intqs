class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for c in strs:
            n = sorted(c)
            hs[str(n)].append(c)
        return [v for v in hs.values()]