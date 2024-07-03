class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        rv = []
        h = defaultdict(list)
        for num in arr:
            h[str(bin(num)).count('1')].append(num)
        for key in sorted(h.keys()):
            rv.extend(sorted(h[key]))
        return rv