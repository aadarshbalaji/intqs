class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = 0
        bottom = n - 1
        while top < bottom:
            for c in range(n):
                temp = matrix[top][c]
                matrix[top][c] = matrix[bottom][c]
                matrix[bottom][c] = temp
            top += 1
            bottom -= 1
        

        for row in range(n):
            for col in range(row+1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        
