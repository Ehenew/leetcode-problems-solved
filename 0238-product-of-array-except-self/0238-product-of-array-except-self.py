class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 6] -> prefix
        # nums = [1,2,3,4]
        # [24, 12, 4, 1] -> suffix

        # Output: [24,12,8,6] => 
        
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(n - 1):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        result = []
        for i in range(n):
           result.append(prefix[i] * suffix[i])

        return result