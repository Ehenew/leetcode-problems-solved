class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Append a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)  # Recurse for the next position
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (swap back)

        backtrack(0)  # Start the backtracking from the first index
        return result