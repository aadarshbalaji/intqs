class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        rv = []
        visited = set()
        def dfs(index, path):
            if (index, str(path)) in visited:
                return 
            if index >= len(nums):
                rv.append(list(path))
                return
            visited.add((index, str(path)))
            dfs(index + 1, path + [nums[index]])
            dfs(index+1, path)
        dfs(0, [])
        return rv
            
