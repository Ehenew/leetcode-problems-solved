class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(idx, path_sum):           
            if idx == len(nums):
                if path_sum == target:
                    return 1
                else:
                    return 0

            if (idx, path_sum) not in memo:
            
                memo[(idx, path_sum)] = dfs(idx + 1,  path_sum + nums[idx]) + dfs(idx + 1, path_sum - nums[idx])

            return memo[(idx, path_sum)]

        return dfs(0,0)


