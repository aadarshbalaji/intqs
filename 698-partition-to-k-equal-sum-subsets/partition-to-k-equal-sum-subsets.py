class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        arr.sort(reverse=True)
        totalsum = sum(arr)
        if totalsum % k != 0:
            return False
        target = totalsum // k
        memo = {}
        taken = ['0'] * len(arr)
        def canmake(index, count, currsum):
            if count == k - 1:
                return True
            takenstr = ''.join(taken)
            if currsum > target:
                memo[takenstr] = False
                return False
            if takenstr in memo:
                return memo[takenstr]
            if currsum == target:
                memo[takenstr] = canmake(0, count + 1, 0)
                return memo[takenstr]
            for j in range(index, len(arr)):
                if taken[j] == '0':
                    taken[j] = '1'
                    if canmake(j+1, count, currsum+arr[j]):
                        return True
                    taken[j] = '0'
            memo[takenstr] = False
            return False
        return canmake(0,0,0)

