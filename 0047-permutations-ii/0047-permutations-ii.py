from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, visited):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                curr.append(nums[i])
                backtrack(curr, visited)
                curr.pop()
                visited[i] = False

        nums.sort()
        res = []
        backtrack([], [False] * len(nums))
        return res
