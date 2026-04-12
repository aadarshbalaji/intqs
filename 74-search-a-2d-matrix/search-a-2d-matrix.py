class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def helper(row):
            l = 0
            r = len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif target < matrix[row][mid]:
                    r = mid -1
                elif target > matrix[row][mid]:
                    l = mid + 1
            return False
        
        lrow = 0
        rrow = len(matrix) - 1
        midrow = -1
        while lrow <= rrow:
            midrow = (lrow + rrow) // 2
            startingmid = matrix[midrow][0]
            if (target < startingmid):
                rrow = midrow - 1
            elif (target >= startingmid and target <= matrix[midrow][-1]):
                return helper(midrow)
            else:
                lrow = midrow + 1

        return False


        