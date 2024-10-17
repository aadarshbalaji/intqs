class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def helper(path, index):
            ans.append(list(path))
            for i in range(index, len(nums)):
                currpath = path + [nums[i]]
                helper(currpath, i + 1)
                currpath.pop()

        helper([], 0)
        return ans