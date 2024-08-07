class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def countOver(A, B, x, y):
            count = 0 
            for i in range(n):
                for j in range(n):
                    if i + x < 0 or i + x >= n or j + y < 0 or j + y >= n:
                        continue
                    else:
                        if A[i][j] + B[i+x][j+y] == 2:
                            count += 1
            return count
        n = len(img1)
        largest = 0
        for x in range(-n + 1, n):
            for y in range(-n+1, n):
                largest = max(largest, countOver(img1, img2, x, y))
        return largest
