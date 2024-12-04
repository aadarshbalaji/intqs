class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minatrow = [float('inf') for i in range(len(triangle))]
        cache = {}
        def search(index, row, currsum):
            if row >= len(triangle) or index >= len(triangle[row]):
                return 0
            if (index, row) in cache:
                return cache[(index, row)]
            ans = triangle[row][index] + min(search(index, row+1, currsum + triangle[row][index]), search(index+1, row+1, currsum + triangle[row][index]))
            cache[(index, row)] = ans
            return ans
        return search(0, 0, 0)