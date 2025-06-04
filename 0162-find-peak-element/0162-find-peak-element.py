class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = -1
        max = float('-inf')

        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                peak = i
        return peak
