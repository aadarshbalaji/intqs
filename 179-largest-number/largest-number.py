class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #nums.map(key=lambda x: str(x), reverse = True)
        if max(nums) == 0:
            return '0'
        new = map(lambda x: str(x), nums)
        new = list(new)
        new.sort(key=lambda x: x * 10, reverse=True)
        ans = ''
        for string in new:
            ans += string
        return ans