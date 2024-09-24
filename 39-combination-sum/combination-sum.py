class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        globalarr = []
        def canmake(path, index):
            if sum(path) > target:
                return False
            elif sum(path) == target:
                globalarr.append(sorted(path))
            else:
                for i in range(index, len(candidates)):
                    canmake(path+[candidates[i]], i)
        canmake([],0)
        return globalarr
            