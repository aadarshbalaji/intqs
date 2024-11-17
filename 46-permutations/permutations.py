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
                    path.append(num)
                    backtrack(index+1, path)
                    path.pop()
        
        backtrack(0, [])
        return rv