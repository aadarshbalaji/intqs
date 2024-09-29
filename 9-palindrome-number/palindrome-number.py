class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        l = 0
        r = len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -=1
        return True