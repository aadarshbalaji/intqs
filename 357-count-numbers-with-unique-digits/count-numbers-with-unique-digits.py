class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        past = self.countNumbersWithUniqueDigits(n-1)
        tot = 9

        for i in range(1, n):
            tot = tot * (10-i)
        return tot + past


        