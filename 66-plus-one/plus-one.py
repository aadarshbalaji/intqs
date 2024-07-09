class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rv = []
        s = ""
        for num in digits:
            s += str(num)
        news = int(s) + 1
        for digit in str(news):
            rv.append(int(digit))
        return rv