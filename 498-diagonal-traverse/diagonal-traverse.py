class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        returnarr = []
        matrix = mat
        row = 0
        col = 0
        direct = 1
        while True:
            print(mat[row][col], direct, row, col)
            returnarr.append(mat[row][col])
            if direct:
                if row - 1 < 0 and col + 1 < len(matrix[0]):
                    col += 1
                    direct = 1 - direct
                    continue
                elif row - 1 < 0 and col + 1 >= len(matrix[0]):
                    if row + 1 < len(matrix):
                        row += 1
                        direct = 1 - direct
                        continue
                elif row - 1 >= 0 and col + 1 < len(matrix[0]):
                    row -= 1
                    col += 1
                    continue
                elif row + 1 < len(matrix) and col + 1 >= len(matrix[0]):
                    row += 1
                    direct = 1 - direct
                    continue
                break
            else:
                if row + 1 >= len(matrix) and col + 1 < len(matrix[0]):
                    col += 1
                    direct = 1 - direct
                    continue
                elif row + 1 < len(matrix) and col - 1 < 0:
                    row += 1
                    direct = 1 - direct
                    continue
                elif row + 1 < len(matrix) and col - 1 >= 0:
                    row += 1
                    col -= 1
                    continue
                break
                
        return returnarr