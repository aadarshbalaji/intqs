class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        totalsum = sum(arr)
        arr.sort(reverse=True)
        if totalsum % k != 0:
            return False
        target = totalsum // k
        taken = ['0'] * n
        memo = {}

        def backtrack(index, count, currsum):
            if count == k - 1:
                return True
            if currsum > target:
                return False

            takenstr = "".join(taken)
            if takenstr in memo:
                return memo[takenstr]    
            if currsum == target:
                memo[takenstr] = backtrack(0, count+1, 0)
                return memo[takenstr]
            
            for j in range(index, n):
                if taken[j] == '0':
                    taken[j] = '1'
                    if backtrack(j+1,count,currsum + arr[j]):
                        return True
                    taken[j] = '0'
            
            memo[takenstr] = False
            return memo[takenstr]
        
        return backtrack(0,0,0)
            