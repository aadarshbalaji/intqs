class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        copy = matrix
        while copy:
            middle = len(copy) // 2
            if copy[middle][0] > target:
                copy = copy[0:middle]
            elif copy[middle][-1] < target:
                copy = copy[middle + 1:]
            else:
                cc = copy[middle]
                while cc:
                    cmid = len(cc)//2
                    if cc[cmid] == target:
                        return True
                    elif cc[cmid] < target:
                        cc = cc[cmid+1:]
                    else:
                        cc = cc[0:cmid]
                return False
            