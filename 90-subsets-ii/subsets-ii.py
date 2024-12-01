class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        hs = set()
        rv = []
        def explore(index, path):
            if index == len(nums):
                key = str(sorted(path))
                if key not in hs:
                    rv.append(sorted(path))
                    hs.add(key)
                return
            use = path + [nums[index]]
            notuse = path
            explore(index + 1, use)
            explore(index + 1, notuse)
        explore(0, [])
        return rv