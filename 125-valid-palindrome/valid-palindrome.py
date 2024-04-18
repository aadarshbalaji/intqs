class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        total = "abcdefghijklmnopqrstuvwxyz0123456789"
        for char in s:
            char = char.lower()
            #print(char)
            if char in total:
                x += char
        return x[::-1] == x       