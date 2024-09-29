class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        curr = 0
        for i, num in enumerate(citations):
            print(n-i, num)
            if n - i <= num:
                curr = max(curr, n-i)
        return curr