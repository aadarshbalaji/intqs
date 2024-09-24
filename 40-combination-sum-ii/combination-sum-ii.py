class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(target, start, comb):
            if target < 0:
                return 
            elif target == 0:
                ans.append(comb)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], i+1, comb+[candidates[i]])
        dfs(target, 0, [])
        return ans