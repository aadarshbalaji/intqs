class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rv = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                rv.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remaining:
                    return
                
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.remove(candidates[i])
        
        backtrack(0,[],target)
        return rv