class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for c in strs:
            n = sorted(c)
            hs[tuple(n)].append(c)
        return [v for v in hs.values()]