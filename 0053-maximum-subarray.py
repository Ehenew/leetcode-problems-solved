class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]  
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Choose between adding the current num or starting a new subarray
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed
        
        return max_sum
