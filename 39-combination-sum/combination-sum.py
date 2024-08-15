class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        globalarr = []
        def canmake(listnum):
            if sum(listnum) > target:
                return False
            elif sum(listnum) == target:
                currlistnum = sorted(listnum)
                if currlistnum in globalarr:
                    return False
                globalarr.append(sorted(listnum))
                return True
            for num in candidates:
                canmake(listnum + [num])
        for num in candidates:
            canmake([num])
        return globalarr
            