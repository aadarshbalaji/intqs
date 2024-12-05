class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hs = defaultdict(int)
        for row in matrix:
            key = ''.join("T" if x == row[0] else 'F' for x in row)
            hs[key] += 1
        return max(hs.values())