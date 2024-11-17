class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rv = []
        def backtrack(index, path):
            if len(path) == len(nums):
                rv.append(list(path))
                return
            for num in nums:
                if num not in path:
                    new = path + [num]
                    backtrack(index+1, new)
        
        backtrack(0, [])
        return rv