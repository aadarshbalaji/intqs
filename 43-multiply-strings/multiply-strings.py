class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        print(type(num1))
        ans1 = 0
        currfor1 = 0
        for digit in reversed(num1):
            ans1 += int(digit) * 10**currfor1
            currfor1 += 1
        ans2 = 0
        currfor2 = 0
        for digit in reversed(num2):
            ans2 += int(digit) * 10**currfor2
            currfor2 += 1
        return str(ans1 * ans2)