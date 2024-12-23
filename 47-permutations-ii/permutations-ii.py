class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        rv = []
        hs = set()
        def helper(currlist, setind):
            if len(currlist) >= len(nums):
                if str(currlist) in hs:
                    return
                rv.append(list(currlist))
                hs.add(str(currlist))
                return
            for i in range(len(nums)):
                if i not in setind:
                    setind.add(i)
                    helper(currlist + [nums[i]], setind)
                    setind.remove(i)
        helper([], set())
        return rv