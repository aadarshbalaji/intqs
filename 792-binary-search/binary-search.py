class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums2 = nums
        x = 0
        while nums2:
            middle = len(nums2)//2
            if nums2[middle] == target:
                return middle + x
            elif nums2[middle] < target:
                nums2 = nums2[middle+1:]
                x += middle + 1
            elif nums2[middle] > target:
                nums2 = nums2[0:middle]
        return -1




        