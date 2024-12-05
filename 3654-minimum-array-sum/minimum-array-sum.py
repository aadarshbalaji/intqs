import math

class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        memo = {}

        def do(index, left1, left2):
            if index >= len(nums):
                return 0

            if (index, left1, left2) in memo:
                return memo[(index, left1, left2)]

            leave = nums[index] + do(index + 1, left1, left2)
            l1 = l2 = both = float('inf')

            if left1 > 0:
                l1 = math.ceil(nums[index] / 2) + do(index + 1, left1 - 1, left2)

            if left2 > 0 and nums[index] >= k:
                l2 = (nums[index] - k) + do(index + 1, left1, left2 - 1)

            if left1 > 0 and left2 > 0:
                # Correctly consider both options for applying both operations
                both1 = math.ceil(nums[index] / 2)
                both2 = nums[index] - k
                if both1 >= k:
                    both = min(both1 - k + do(index + 1, left1 - 1, left2 - 1),
                            math.ceil(both2 / 2) + do(index + 1, left1 - 1, left2 - 1))
                elif both2 >= 0:
                    both = math.ceil(both2 / 2) + do(index + 1, left1 - 1, left2 - 1)

            ans = min(leave, l1, l2, both)
            memo[(index, left1, left2)] = ans
            return ans

        return do(0, op1, op2)