class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            r += n % 2
            n = n >> 1
        return r
        