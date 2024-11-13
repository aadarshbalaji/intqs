class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            c = sorted(s)
            ans[str(c)].append(s)
        return [v for v in ans.values()]