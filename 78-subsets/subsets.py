class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def create(index, path):
            ans.append(list(path))
            for i in range(index, len(nums)):
                currpath = list(path) + [nums[i]]
                create(i+1, currpath)
                currpath.remove(nums[i])
            
        create(0,[])
        return ans