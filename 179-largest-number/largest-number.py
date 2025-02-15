class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        arr = list(map(str, nums))
        arr.sort(key = lambda x: x*10, reverse=True)
        if arr[0] == '0':
            return '0'
        
        return ''.join(arr)


