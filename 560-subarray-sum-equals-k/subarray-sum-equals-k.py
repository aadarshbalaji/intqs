class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pres = {0:1}
        prefix_sum = 0
        count = 0 
        for num in nums:
            prefix_sum += num
            if prefix_sum -k in pres:
                count += pres[prefix_sum-k]
            if prefix_sum in pres:
                pres[prefix_sum]  += 1
            else:
                pres[prefix_sum]  = 1
        #print(pres)
        return count
