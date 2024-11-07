class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenrows = len(matrix)
        lencols = len(matrix[0])
        cols = []
        rows = []
        for r in range(lenrows):
            for c in range(lencols):
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)
        for row in rows:
            matrix[row] = [0] * lencols
        for col in cols:
            for roow in range(lenrows):
                matrix[roow][col] = 0
        

        