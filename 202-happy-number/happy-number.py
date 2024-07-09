class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n != 1:
            newn = 0
            if n in hset:
                return False
            hset.add(n)
            for digit in str(n):
                newn += int(digit) ** 2
            n = newn   

        return True