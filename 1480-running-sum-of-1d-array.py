class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array = [0] * len(nums)

        for i in range(len(nums)):
            sum_array[i] = sum_array[i - 1] + nums[i]

        return sum_array
