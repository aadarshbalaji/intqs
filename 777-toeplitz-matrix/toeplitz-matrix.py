class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        lookfirst = 0
        for i in range(len(matrix[0])-1):
            startingrow = 0
            startingcol = i
            currval = matrix[startingrow][startingcol]
            while startingrow < len(matrix) and startingcol < len(matrix[0]):
                if matrix[startingrow][startingcol] == currval:
                    startingrow += 1
                    startingcol += 1
                else:
                    return False
        for i in range(1,len(matrix) - 1):
            startings = i
            copyi = 0
            currval = matrix[startings][copyi]
            while startings < len(matrix) and copyi < len(matrix[0]):
                if matrix[startings][copyi] == currval:
                    startings += 1
                    copyi += 1
                else:
                    return False
        return True

            