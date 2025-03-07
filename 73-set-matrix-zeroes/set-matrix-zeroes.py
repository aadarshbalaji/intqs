class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        lenrows = len(matrix)
        lencols = len(matrix[0])
        
        for row in range(lenrows):
            for col in range(lencols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        
        for row in range(lenrows):
            for col in range(lencols):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0