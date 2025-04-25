class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # Place nums[i] at the correct index if it's in the range [1, n]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # After placement, the first index where nums[i] != i + 1 is our answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in place, the missing number is n + 1
        return n + 1
